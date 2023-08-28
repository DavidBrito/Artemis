"""Module provinding users routes"""

from flask import Blueprint

from src.errors.flask_restful_api import ExtendedAPI
from ..controllers.sessions_controller import SessionsController

sessions_bp = Blueprint("sessions", __name__)
sessions = ExtendedAPI(sessions_bp)

"""Routes"""
sessions.add_resource(SessionsController, "/")
