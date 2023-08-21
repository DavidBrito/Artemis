"""Module provinding all project Models"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def init_database(app):
    """Database initializer function"""
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)


