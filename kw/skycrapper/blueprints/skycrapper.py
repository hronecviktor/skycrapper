from ..settings import STALL_MAPPING

from quart import Blueprint
from quart import current_app
from quart import make_response


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
    pass


@skycrapper.route('/data', methods=['GET'])
async def test():
    """
    Get the stats
    :return:
    """
    # SQLITE DB
    db = current_app.db
    pass
