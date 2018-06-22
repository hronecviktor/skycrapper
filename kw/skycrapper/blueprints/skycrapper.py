from datetime import datetime

from quart import Blueprint
from quart import current_app
from quart import make_response

from ..settings import STALL_MAPPING

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
    return await make_response('Shit has been registered', 401)


@skycrapper.route('/data', methods=['GET'])
async def test():
    """
    Get the stats
    :return:
    """
    # SQLITE DB
    db = current_app.db
    pass


@skycrapper.route('/show', methods=['GET'])
async def show():
    """
    Dumps shits table for test
    :return:
    """
    db = current_app.db
    cur = db.cursor()
    cur.execute('''SELECT * FROM shits''')
    return await make_response(str(cur.fetchall()))
