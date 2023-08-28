"""Module provinding User service """

from flask_jwt_extended import create_access_token
from src.utils import bcrypt
from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository


class AuthenticateService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self, username, password):
        """Main method that executes the service"""

        user = self.__users_repository.find_by_username(username)

        if not user:
            raise AppError(401, message="Invalid username or password")

        if not bcrypt.check_password_hash(user["password"], password):
            raise AppError(401, message="Invalid username or password")

        del user["password"]

        session_token = create_access_token(identity=user, expires_delta=False)

        return {"session_token": session_token, "user": user}
