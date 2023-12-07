import os
from pathlib import Path

import app.routes as routes
from app.extensions import db, migrate
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv(dotenv_path=Path('../.env'))


def create_app():
    app = Flask(__name__)
    CORS(app)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    # TODO: Is track modification needed? If there are more parameters, this could be automated using a loop.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(routes.url)


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=80)
