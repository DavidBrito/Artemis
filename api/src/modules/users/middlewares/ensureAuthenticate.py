"""Module providing Authenticated middlewares"""

from src.utils import jwt
from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository

# from flask_jwt_extended import current_user

users_repository = UsersRepository()


@jwt.user_lookup_loader
def ensure_authenticated(_jwt_header, jwt_data):
    """
    Validating if authenticated user exists in the database and
    loads it into flask_jwt_extended current_user object
    """

    identity = jwt_data["sub"]

    if not identity or not identity.get("id") or not identity.get("username"):
        raise AppError(401, "Invalid token")

    user = users_repository.find_by_id(identity.get("id"))

    if not user:
        raise AppError(401, "User does not exist")

    return user
