from collections import defaultdict
from datetime import datetime, timedelta

import arrow
from quart import Blueprint
from quart import current_app
from quart import make_response

from ..settings import STALL_MAPPING

REVERSE_MAPPING = {value: key for key, value in STALL_MAPPING.items()}

skycrapper = Blueprint('skycrapper', __name__)


@skycrapper.route('/ping', methods=['GET'])
async def ping():
    return await make_response('pong')


@skycrapper.route('/shit/<stall>', methods=['POST'])
async def shit(stall):
    """
    Register a shit taken
    :param stall:
    :return:
    """
    db = current_app.db
    cur = current_app.db.cursor()
    cur.execute('''INSERT INTO shits VALUES (?, ?)''', (STALL_MAPPING[stall], datetime.utcnow()))
    db.commit()
    return await make_response('Shit has been registered', 201)


@skycrapper.route('/data', methods=['GET'])
async def test():
    """
    Get the stats
    :return:
    """
    cur = current_app.db.cursor()
    cur.execute('''SELECT * FROM shits''')
    data = cur.fetchall()
    turdpile = defaultdict(float)
    for stall, t_shit in data:
        turd_age = (arrow.get(datetime.utcnow()) - arrow.get(t_shit))
        if turd_age.seconds and turd_age < timedelta(hours=12):
            turdpile[REVERSE_MAPPING[stall]] += (turd_age.seconds / 60) ** -1
    return await make_response(str(dict(turdpile)))


@skycrapper.route('/show', methods=['GET'])
async def show():
    """
    Dumps shits table for test
    :return:
    """
    cur = current_app.db.cursor()
    cur.execute('''SELECT * FROM shits''')
    return await make_response(str(cur.fetchall()))
