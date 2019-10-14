from flask import Blueprint
from src.controllers.coregalineiro import CoreGalineiro

galineiro = Blueprint('galineiro', __name__)

@galineiro.route('/abrir_porta')
def abrir_porta():
    return {'PORTA_ABERTA': CoreGalineiro.instance().abrir_porta()}

@galineiro.route('/pechar_porta')
def pechar_porta():
    return {'PORTA_PECHADA': CoreGalineiro.instance().cerrar_porta()}

@galineiro.route('/encender_luz')
def encender_luz():
    return {'LUZ_ENCENDIDA': CoreGalineiro.instance().encender_luz()}

@galineiro.route('/apagar_luz')
def apagar_luz():
    return {'LUZ_APAGADA': CoreGalineiro.instance().apagar_luz()}

@galineiro.route('/')
def hello():
    return "HOLA"
