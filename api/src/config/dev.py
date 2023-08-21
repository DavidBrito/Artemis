"""Module provinding project environment variables and config"""

import os
from dotenv_vault import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Dev config"""

    # JWT_SECRET_KEY = os.getenv("FLASK_JWT_SECRET_KEY")
    # SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
