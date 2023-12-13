from flask import Flask
from flask_login import current_user

from app.extensions import db, migrate, login_manager
from app.user.models import User
from app.config import Config
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
    register_login_manager(app)


def register_login_manager(app):
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.context_processor
    def inject_user():
        return dict(user=current_user)

def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(post.views.blueprint)


