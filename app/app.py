from flask import Flask, render_template

from app.extensions import db, migrate
from config import Config
from app.user import models

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    # Register blueprints here

    @app.route('/')
    def test_page():
        return render_template('home.html')

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
