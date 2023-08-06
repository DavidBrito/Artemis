"""Module provinding project starting script"""

from server import create_app

if __name__ == "__main__":
    app = create_app("default_config")
    app.run(debug=False)
