from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User

class UserRegistrationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', required=True)
        self.parser.add_argument('password', required=True)
        self.parser.add_argument('email', required=True)

    def post(self):
        data = self.parser.parse_args()
        username = data['username']
        password = data['password']
        email = data['email']

        user_model = User(username)
        registration_result = user_model.register_user(username, password, email)

        return registration_result

class UserLoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', required=True)
        self.parser.add_argument('password', required=True)

    def post(self):
        data = self.parser.parse_args()
        username = data['username']
        password = data['password']

        user_model = User(username)
        authenticated_user = user_model.authenticate(username, password)

        if authenticated_user:
            access_token = create_access_token(identity=authenticated_user.id)
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401
