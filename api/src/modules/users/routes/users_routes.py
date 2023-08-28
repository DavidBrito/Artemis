"""Module provinding users routes"""

from flask import Blueprint

from src.errors.flask_restful_api import ExtendedAPI
from ..controllers.users_controller import UsersController

users_bp = Blueprint("users", __name__)
users = ExtendedAPI(users_bp)

"""Routes"""
users.add_resource(UsersController, "/")
