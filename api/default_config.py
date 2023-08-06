"""Module provinding project environment variables and config"""

import os
from dotenv_vault import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
