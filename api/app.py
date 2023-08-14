"""Module provinding project starting script"""

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from src.routes_v1 import api_bp

jwt = JWTManager()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_environment="dev"):
    """Function that initialize app with specified config"""
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config.from_object(f"src.config.{config_environment}.Config")

    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    import src.database.models

    app.register_blueprint(api_bp, url_prefix="/v1")
    CORS(app)

    return app


if __name__ == "__main__":
    app_instance = create_app()
    app_instance.run(debug=True)
