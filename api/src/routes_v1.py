"""Module provinding project routes"""

from flask import Blueprint

from .modules.users.routes.users_routes import users_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(users_bp, url_prefix="/users")
