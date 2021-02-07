from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(app_name='FORKME'):

    # Get the app
    app = Flask(app_name)
    Bootstrap(app)

    # Register /fork blueprint.
    from app.fork import fork
    app.register_blueprint(fork, url_prefix='/fork')

    return app
