"""Module provinding User service """

from ..database.repositories.users_repository import UsersRepository


class ShowAllUsersService:
    """Service's class"""

    def __init__(self):
        self.__users_repository = UsersRepository()

    def execute(self):
        """Main method that executes the service"""

        return self.__users_repository.find_all()
