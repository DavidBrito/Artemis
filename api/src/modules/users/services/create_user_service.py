"""Module provinding User service """

from src.errors.app_error import AppError
from ..database.repositories.users_repository import UsersRepository


class CreateUserService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self, email, username, password):
        """Main method that executes the service"""

        find_user = self.__users_repository.find_by_username(username)

        if find_user:
            raise AppError(400, message="Username already used")

        user = self.__users_repository.create(
            email=email, username=username, password=password
        )
        print(user)

        return user
