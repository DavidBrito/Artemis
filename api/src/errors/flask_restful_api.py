"""Module providing custom flask restful api for handle error method"""

from flask import jsonify
from flask_restful import Api
from flask_jwt_extended.exceptions import JWTExtendedException
from jwt import PyJWTError
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException


class ExtendedAPI(Api):
    """
    This class overrides 'handle_error' method of 'Api' class,
    to extend global exception handling functionality of 'flask-restful'.
    """

    def handle_error(self, e):
        """
        It helps preventing writing unnecessary try/except block though out the application
        """

        print(e, type(e))

        # Handle HTTPExceptions
        if isinstance(e, HTTPException):
            return (
                jsonify(
                    {
                        "message": getattr(
                            e, "description", HTTP_STATUS_CODES.get(e.code, "")
                        ),
                        "data": getattr(e, "data", {}).get("message"),
                    }
                ),
                e.code,
            )

        # Handle FLASK_JWT_EXTENDEDExceptions
        if isinstance(e, JWTExtendedException) or isinstance(e, PyJWTError):
            return (
                jsonify(
                    {
                        "message": str(e),
                    }
                ),
                401,
            )

        # If msg attribute is not set, consider it as Python core exception
        # and hide sensitive error info from end user
        if not getattr(e, "message", None) or not getattr(e, "msg", None):
            return jsonify({"message": "Internal server error"}), 500

        # Handle application specific custom exceptions
        return jsonify(**e.kwargs), e.http_status_code
