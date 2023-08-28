"""Module provinding project environment variables and config"""

import os
import json
from dotenv_vault import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Prod config"""

    # JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")
    JWT_COOKIE_SECURE = os.getenv("FLASK_JWT_COOKIE_SECURE") == "False"
    JWT_TOKEN_LOCATION = json.loads(os.getenv("FLASK_JWT_TOKEN_LOCATION"))
    # SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
