from flask import Flask
from .config import app_config
import os

app = Flask(__name__)

env_name = os.getenv('FLASK_ENV') or 'production'
app.config.from_object(app_config[env_name])
