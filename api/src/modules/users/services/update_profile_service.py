"""Module provinding User service """

from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository


class UpdateProfileService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self, user_id, username, email, password):
        """Main method that executes the service"""

        user = self.__users_repository.find_by_id(user_id, dump=False)

        if not user:
            raise AppError(404, message="User not found")

        user.email = email
        user.password = password

        new_user = self.__users_repository.save(user)

        return new_user
