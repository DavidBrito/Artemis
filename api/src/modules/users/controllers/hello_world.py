"""Module provinding Hello_World Controller Methods"""

from flask_restful import Resource
from ..services.hello_world_service import HelloWorldService


class HelloWorld(Resource):
    """Controller's class"""

    def get(self):
        """GET Method that returns hello world"""

        response = HelloWorldService().execute()

        return response
