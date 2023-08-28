"""Module provinding Session Controller Methods"""

from flask_restful import Resource, reqparse, fields, marshal_with
from ..services.authenticate_service import AuthenticateService


class SessionsController(Resource):
    """Controller's class"""

    __RETURN_USER_FIELDS = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
        "created_at": fields.String,
        "updated_at": fields.String,
    }

    __RETURN_SESSION_FIELDS = {
        "session_token": fields.String,
        "user": fields.Nested(__RETURN_USER_FIELDS),
    }

    @marshal_with(__RETURN_SESSION_FIELDS)
    def post(self):
        """POST Method that authenticates a user"""

        parser = reqparse.RequestParser(trim=True)
        parser.add_argument(
            "username",
            type=str,
            required=True,
            nullable=False,
            help="required",
        )
        parser.add_argument(
            "password",
            type=str,
            required=True,
            nullable=False,
            help="required",
        )

        args = parser.parse_args(strict=True)

        authenticate = AuthenticateService()
        session_fields = authenticate.execute(
            username=args.username, password=args.password
        )

        return session_fields
