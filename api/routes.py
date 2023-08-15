"""Module provinding project routes"""

from flask import Blueprint
from flask_restful import Api

from controllers.user_controller import UserLoginResource
from controllers.user_controller import UserRegistrationResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Routes
api.add_resource(UserLoginResource, "/login")
api.add_resource(UserRegistrationResource, "/register")

