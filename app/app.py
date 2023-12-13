from flask import Flask, render_template

from app.extensions import db, migrate
from config import Config
from app import user, public, post

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(post.views.blueprint)
