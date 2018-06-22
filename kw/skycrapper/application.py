import sqlite3
import logging

from quart import Quart

from .blueprints.skycrapper import skycrapper


def create_app():
    app = Quart(__name__)

    @app.before_first_request
    async def init_sessions():
        app.db = sqlite3.connect('db')

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.register_blueprint(skycrapper)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
