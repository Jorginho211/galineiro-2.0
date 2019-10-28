from functools import wraps
from flask import request, Response
import json

with open('src/routes/v1/config.json', 'r') as f:
    config = json.load(f)

username = config['auth']['username']
password = config['auth']['password']

def check(usernameIn, passwordIn):
    return usernameIn == username and passwordIn == password

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def basic(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated