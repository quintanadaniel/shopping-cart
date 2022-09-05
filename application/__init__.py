from http import HTTPStatus

from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .home import home
        from .status import status

        app.register_blueprint(home.home_bp)
        app.register_blueprint(status.status_bp)

    return app


def page_not_found(error):
    return "<h1>Page not found or not correct</h1>", HTTPStatus.NOT_FOUND
