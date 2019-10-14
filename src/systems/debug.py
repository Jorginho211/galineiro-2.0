from .base import SystemBase
import time

class Debug(SystemBase):
    def __init__(self):
        super().__init__()
        self.__intervalo_pulsador = None
        self.__intervalo_dia = None
        self.__estado_pulsador = None
        self.__estado_dia = None


    def encender_fuente(self):
        print("fuente encendida")

    def apagar_fuente(self):
        print("fuente apagada")

    def abrir_porta(self):
        self._cadeado_porta.acquire()
        print("porta aberta")
        self._cadeado_porta.release()

    def pechar_porta(self):
        self._cadeado_porta.acquire()
        print("porta pechada")
        self._cadeado_porta.release()

    def e_dia(self):
        if self.__estado_dia == None or time.time() >= self.__intervalo_dia:
            self.__estado_dia = bool(int(input('0 -> Noite, 1 -> Dia: ')))
            self.__intervalo_dia = time.time() + 20

        return self.__estado_dia

    def encender_incandescente(self):
        print("luz encendida")

    def apagar_incandescente(self):
        print("luz apagada")

    def encender_luz_pulsador(self):
        print("encendido luz pulsador")

    def apagar_luz_pulsador(self):
        print("apagado luz pulsador")

    def esta_pulsado(self):
        if self.__estado_pulsador == None or time.time() >= self.__intervalo_pulsador:
            self.__estado_pulsador = bool(int(input('0 -> Sin pulsar, 1 -> Pulsado: ')))
            self.__intervalo_pulsador = time.time() + 20
            return self.__estado_pulsador

        return False