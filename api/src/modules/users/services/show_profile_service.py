"""Module provinding User service """

from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository


class ShowProfileService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self, user_id):
        """Main method that executes the service"""

        user = self.__users_repository.find_by_id(user_id)

        if not user:
            raise AppError(404, message="User not found")

        return user
