from flask import Blueprint, render_template, Response
from src.controllers.coregalineiro import CoreGalineiro

galineiro = Blueprint('galineiro', __name__, static_folder='static', template_folder='templates')

@galineiro.route('/abrir_porta')
def abrir_porta():
    return {'codigo': CoreGalineiro.instance().abrir_porta()}

@galineiro.route('/pechar_porta')
def pechar_porta():
    return {'codigo': CoreGalineiro.instance().cerrar_porta()}

@galineiro.route('/encender_luz')
def encender_luz():
    return {'LUZ_ENCENDIDA': CoreGalineiro.instance().encender_luz()}

@galineiro.route('/apagar_luz')
def apagar_luz():
    return {'LUZ_APAGADA': CoreGalineiro.instance().apagar_luz()}

@galineiro.route('/')
def index():
    return render_template('index.html')

@galineiro.route('/activar_manual')
def activar_manual():
    return {'manAuto': CoreGalineiro.instance().estado_manual_mobil(True)}

@galineiro.route('/desactivar_manual')
def desactivar_manual():
    return {'manAuto': CoreGalineiro.instance().estado_manual_mobil(False)}

@galineiro.route('/parametros')
def parametros():
    return CoreGalineiro.instance().parametros()

@galineiro.route('/sacar_foto')
def sacar_foto():
    return { 'data': CoreGalineiro.instance().sacar_foto() }
