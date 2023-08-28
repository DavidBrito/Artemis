"""Module provinding project starting script"""

from flask import Flask
from flask_cors import CORS

from src.routes_v1 import api_bp
from src.database.sqlalchemy import init_database
from src.utils import init_utilities


def create_app(config_environment="dev"):
    """Function that initialize app with specified config"""
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config.from_object(f"src.config.{config_environment}.Config")

    init_utilities(app)
    init_database(app)

    app.register_blueprint(api_bp, url_prefix="/v1")
    CORS(app)

    return app


if __name__ == "__main__":
    app_instance = create_app()
    app_instance.run(debug=True)
