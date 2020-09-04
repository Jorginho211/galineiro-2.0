from flask import Blueprint, render_template, Response
from src.controllers.coregalineiro import CoreGalineiro
from .auth import basic as basic_authentication

galineiro = Blueprint('galineiro', __name__, static_folder='static', template_folder='templates')


@galineiro.route('/abrir_porta')
@basic_authentication
def abrir_porta():
    return {'codigo': CoreGalineiro.instance().abrir_porta()}


@galineiro.route('/pechar_porta')
@basic_authentication
def pechar_porta():
    return {'codigo': CoreGalineiro.instance().cerrar_porta()}


@galineiro.route('/encender_luz')
@basic_authentication
def encender_luz():
    return {'LUZ_ENCENDIDA': CoreGalineiro.instance().encender_luz()}


@galineiro.route('/apagar_luz')
@basic_authentication
def apagar_luz():
    return {'LUZ_APAGADA': CoreGalineiro.instance().apagar_luz()}


@galineiro.route('/')
@basic_authentication
def index():
    return render_template('index.html')


@galineiro.route('/activar_manual')
@basic_authentication
def activar_manual():
    return {'manAuto': CoreGalineiro.instance().estado_manual_mobil(True)}


@galineiro.route('/desactivar_manual')
@basic_authentication
def desactivar_manual():
    return {'manAuto': CoreGalineiro.instance().estado_manual_mobil(False)}

@galineiro.route('/parametros')
@basic_authentication
def parametros():
    return CoreGalineiro.instance().parametros()


@galineiro.route('/sacar_foto')
@basic_authentication
def sacar_foto():
    return {'data': CoreGalineiro.instance().sacar_foto() }
