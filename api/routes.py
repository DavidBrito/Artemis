"""Module provinding project routes"""

from flask import Blueprint
from flask_restful import Api
from controllers.hello_world import HelloWorld

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Routes
api.add_resource(HelloWorld, "/")
