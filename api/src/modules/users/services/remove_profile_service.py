"""Module provinding User service """

from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository


class RemoveProfileService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self, user_id):
        """Main method that executes the service"""

        check_user_exists = self.__users_repository.find_by_id(user_id)

        if not check_user_exists:
            raise AppError(404, message="User not found")

        return self.__users_repository.delete(user_id)
