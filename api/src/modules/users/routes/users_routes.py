"""Module provinding users routes"""

from flask import Blueprint
from flask_restful import Api
from ..controllers.hello_world import HelloWorld

users_bp = Blueprint("users", __name__)
users = Api(users_bp)

"""Routes"""
users.add_resource(HelloWorld, "/")
