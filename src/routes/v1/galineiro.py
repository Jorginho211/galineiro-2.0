from flask import Blueprint

galineiro = Blueprint('galineiro', __name__)

@galineiro.route('/')
def hello():
    return "ola"


