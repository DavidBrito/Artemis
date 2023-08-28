"""Module provinding Profile Controller Methods"""

from flask_restful import Resource, reqparse, fields, inputs, marshal_with
from flask_jwt_extended import jwt_required
from src.utils.regex import RegexList
from ..services.show_profile_service import ShowProfileService
from ..services.update_profile_service import UpdateProfileService
from ..services.remove_profile_service import RemoveProfileService


class ProfilesController(Resource):
    """Controller's class"""

    __RETURN_PROFILE_FIELDS = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
        "created_at": fields.String,
        "updated_at": fields.String,
    }

    @jwt_required()
    @marshal_with(__RETURN_PROFILE_FIELDS, envelope="user")
    def get(self, user_id):
        """GET Method that returns a user profile"""

        show_all_users = ShowProfileService()
        users = show_all_users.execute(user_id)

        return users

    @jwt_required()
    @marshal_with(__RETURN_PROFILE_FIELDS, envelope="user")
    def put(self, user_id):
        """PUT Method that updates a user profile"""

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

        update_user = UpdateProfileService()
        user = update_user.execute(
            user_id=user_id,
            email=args.email,
            username=args.username,
            password=args.password,
        )

        return user, 200

    @jwt_required()
    def delete(self, user_id):
        """DELETE Method that remove a user profile"""

        remove_user = RemoveProfileService()
        remove_user.execute(user_id)

        return "", 204
