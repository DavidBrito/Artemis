"""Module provinding Hello_World Controller Methods"""

from flask_restful import Resource


class HelloWorld(Resource):
    """Controller's class"""

    def get(self):
        """GET Method that returns hello world"""

        return {"hello": "world"}
