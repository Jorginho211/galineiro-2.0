from flask import Flask
from .config import app_config
import os

app = Flask(__name__)

if __name__ == 'main':
    env_name = os.getenv('FLASK_ENV') or 'production'
    app.config.from_object(app_config[env_name])
    app.run(threaded=True)


@app.route("/hello")
def hello():
    return "ola"
