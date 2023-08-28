"""Module provinding project routes"""

from flask import Blueprint

import src.modules.users.middlewares.ensureAuthenticate

from .modules.users.routes.users_routes import users_bp
from .modules.users.routes.profiles_routes import profiles_bp
from .modules.users.routes.sessions_routes import sessions_bp

api_bp = Blueprint("api", __name__)

api_bp.register_blueprint(users_bp, url_prefix="/users")
api_bp.register_blueprint(profiles_bp, url_prefix="/profiles")
api_bp.register_blueprint(sessions_bp, url_prefix="/sessions")
