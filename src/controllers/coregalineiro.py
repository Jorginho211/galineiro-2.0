from threading import Lock
from ..systems import Debug
import subprocess
import time
import base64


class CoreGalineiro:
    __INSTANCE = None

    def __init__(self):
        self.__porta = False
        self.__luz_ciclo = False
        self.__incandescente = False
        self.__pulsador = False
        self.__manual_mobil = False  # FALSE: Automatico TRUE: Manual
        self.__cerre_manual = False  # Evitar a espera de 20 minutos se xa foi feita no peche
        self.__candado_camara = Lock()  # SEMAFORO

        self.__system = Debug()

        self.root_path = None

    @staticmethod
    def instance():
        if CoreGalineiro.__INSTANCE is None:
            CoreGalineiro.__INSTANCE = CoreGalineiro()

        return CoreGalineiro.__INSTANCE

    def sacar_foto(self):
        self.__candado_camara.acquire()
        # -i gspca_zc3xx

        ruta_foto = self.root_path + "/media/galineiro.jpg"

        comando = "fswebcam -d /dev/video0 -r 320x232 -S 10 --jpeg 80 --no-banner --save " + ruta_foto
        camera_process = subprocess.Popen(comando.split())
        camera_process.wait()

        with open(ruta_foto, "rb") as archivo_image:
            base64_imaxe = str(base64.b64encode(archivo_image.read()))
        self.__candado_camara.release()

        return base64_imaxe

    def abrir_porta(self):
        if self.__porta:
            return True

        self.__system.encender_fuente()
        self.__system.abrir_porta()

        if not self.__pulsador:
            self.__system.apagar_fuente()

        self.__porta = True

        return True

    def cerrar_porta(self):
        if not self.__porta:
            return True

        if not self.__pulsador:
            self.__system.encender_fuente()
            self.__system.pechar_porta()
            self.__system.apagar_fuente()
            self.__porta = False
            return True

        return False

    def encender_luz(self):
        if not self.__incandescente:
            self.__system.encender_incandescente()
            self.__incandescente = True

        return True

    def apagar_luz(self):
        if not self.__incandescente:
            return True

        if self.__pulsador or self.__luz_ciclo:
            return False

        self.__system.apagar_incandescente()
        self.__incandescente = False

        return True

    def ciclo(self):
        self.cerrar_porta()
        cerrouse_porta_automaticamente = True   # Cando e de noite a porta cerrase despois de pasar o tempo un unica vez

        while True:
            if self.__system.esta_pulsado():
                if not self.__pulsador:
                    self.__pulsador = True
                    self.__system.encender_luz_pulsador()
                    self.encender_luz()
                    self.abrir_porta()

                elif self.__pulsador:
                    self.apagar_luz()
                    self.__system.apagar_luz_pulsador()
                    self.__pulsador = False

            if not self.__pulsador and not self.__manual_mobil:
                if not self.__system.e_dia():
                    if not cerrouse_porta_automaticamente:
                        self.__luz_ciclo = True
                        self.encender_luz()
                        time.sleep(1200)
                        cerrouse_porta_automaticamente = True
                    self.cerrar_porta()
                    self.apagar_luz()
                    self.__luz_ciclo = False

                else:
                    self.abrir_porta()
                    cerrouse_porta_automaticamente = False