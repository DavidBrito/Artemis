"""Module provinding project starting script"""

from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager
from routes import api_bp

app = Flask(__name__)
jwt = JWTManager(app)


def create_app(config_filename):
    """Function that initialize app with specified config"""

    app.config.from_object(config_filename)

    app.register_blueprint(api_bp, url_prefix="/api")

    CORS(app)

    return app


if __name__ == "__main__":
    app = create_app("default_config")
    app.run(debug=True)
