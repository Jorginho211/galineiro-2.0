from threading import Lock
from ..systems import Debug
import subprocess
import base64


class CoreGalineiro:
    __INSTANCE = None

    def __init__(self):
        self.__porta = 0
        self.__incandescente = 0
        self.__incandescente_movil = 0
        self.__pulsador = 0
        self.__man_auto = 0  # 0: Automatico 1: Manual
        self.__cerre_manual = 0  # Evitar a espera de 20 minutos se xa foi feita no peche
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
        #-i gspca_zc3xx

        ruta_foto = self.root_path + "/media/galineiro.jpg"

        comando = "fswebcam -d /dev/video0 -r 320x232 -S 10 --jpeg 80 --no-banner --save " + ruta_foto
        camera_process = subprocess.Popen(comando.split())
        camera_process.wait()

        with open(ruta_foto, "rb") as archivo_image:
            base64_imaxe = str(base64.b64encode(archivo_image.read()))
        self.__candado_camara.release()

        return base64_imaxe