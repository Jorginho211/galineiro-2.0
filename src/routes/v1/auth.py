from functools import wraps
from flask import request, Response
import os


def check(usernameIn, passwordIn):
    return usernameIn == os.getenv('GALINEIRO_USER') and passwordIn == os.getenv('GALINEIRO_PASSWORD')


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
