"""Module provinding User Controller Methods"""

from flask_restful import Resource, reqparse, fields, inputs, marshal_with
from flask_jwt_extended import jwt_required
from src.utils.regex import RegexList
from ..services.show_all_users_service import ShowAllUsersService
from ..services.create_user_service import CreateUserService


class UsersController(Resource):
    """Controller's class"""

    __RETURN_USER_FIELDS = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
        "created_at": fields.String,
        "updated_at": fields.String,
    }

    @jwt_required()
    @marshal_with(__RETURN_USER_FIELDS, envelope="users")
    def get(self):
        """GET Method that returns all users"""

        show_all_users = ShowAllUsersService()
        users = show_all_users.execute()

        return users

    @jwt_required()
    @marshal_with(__RETURN_USER_FIELDS, envelope="user")
    def post(self):
        """POST Method that creates a user"""

        parser = reqparse.RequestParser(trim=True)
        parser.add_argument(
            "username",
            type=str,
            required=True,
            nullable=False,
            help="required",
        )
        parser.add_argument(
            "email",
            type=inputs.regex(RegexList.EMAIL),
            required=True,
            nullable=False,
            help="Must be a valid email - required",
        )
        parser.add_argument(
            "password",
            type=lambda password: inputs.regex(RegexList.VALID_LENGTH(6))(
                str(password)
            ),
            required=True,
            nullable=False,
            help="Must have at least 6 characters - required",
        )

        args = parser.parse_args(strict=True)

        create_user = CreateUserService()
        user = create_user.execute(
            email=args.email, username=args.username, password=args.password
        )

        return user, 201
