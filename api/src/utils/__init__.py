"""Module provinding all utility objects"""

from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

jwt = JWTManager()
bcrypt = Bcrypt()


def init_utilities(app):
    """Utilities initializer function"""

    jwt.init_app(app)
    bcrypt.init_app(app)
