import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import api_bp

from utils.database import init_db # type: ignore

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

jwt = JWTManager(app)

def create_app(config_filename):
    app.config.from_object(config_filename)

    app.register_blueprint(api_bp, url_prefix="/api")

    CORS(app)

    init_db()

    return app

if __name__ == "__main__":
    app = create_app("default_config")
    app.run(debug=True)
