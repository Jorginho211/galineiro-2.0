from flask import Flask
from .config import app_config
from .routes.v1 import galineiro
import os

app = Flask(__name__)

env_name = os.getenv('FLASK_ENV') or 'production'
app.config.from_object(app_config[env_name])

app.register_blueprint(galineiro, url_prefix='/api/v1/galineiro')