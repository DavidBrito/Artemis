"""Module provinding profiles routes"""

from flask import Blueprint

from src.errors.flask_restful_api import ExtendedAPI
from ..controllers.profiles_controller import ProfilesController

profiles_bp = Blueprint("profiles", __name__)
profiles = ExtendedAPI(profiles_bp)

"""Routes"""
profiles.add_resource(ProfilesController, "/<int:user_id>")
