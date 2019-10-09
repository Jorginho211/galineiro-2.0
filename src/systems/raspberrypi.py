from .base import SystemBase
import time
import RPi.GPIO as GPIO

class RaspberryPi(SystemBase):
    def __init__(self):
        super.__init__()

        self.__lampara_pin = 7              # Lampara Incandescente Cortello
        self.__transformador_24v_pin = 15   # Alimentación Transformado 24 V CC
        self.__motor_comun_pin = 18         # - 0 V CC Motor Puerta
        self.__motor_sentido1_pin = 23      # + 24 V CC Motor Puerta (SEMTIDO 1)
        self.__motor_sentido2_pin = 24      # + 24 V CC Motor Puerta (Sentido 2)
        self.__luz_pulsador = 25            # Luz Pulsador MAN/AUTO

        self.__pulsador = 20
        self.__noite = 16
        self.__dia = 12

        self.__tempo_apertura_peche = 22

        self.__inicializar_pins__()

    def __inicializar_pins__(self):

        # Establecemos mecanismo de numeracion
        GPIO.setmode(GPIO.BCM)

        # Configuracion saidas
        GPIO.setup(self.__lampara_pin, GPIO.OUT)
        GPIO.output(self.__lampara_pin, True)
        GPIO.setup(self.__transformador_24v_pin, GPIO.OUT)
        GPIO.output(self.__transformador_24v_pin, True)
        GPIO.setup(self.__motor_comun_pin, GPIO.OUT)
        GPIO.output(self.__motor_comun_pin, True)
        GPIO.setup(self.__motor_sentido1_pin, GPIO.OUT)
        GPIO.output(self.__motor_sentido1_pin, True)
        GPIO.setup(self.__motor_sentido2_pin, GPIO.OUT)
        GPIO.output(self.__motor_sentido2_pin, True)
        GPIO.setup(self.__luz_pulsador, GPIO.OUT)
        GPIO.output(self.__luz_pulsador, True)

        # Configuracion entradas
        GPIO.setup(self.__pulsador, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pulsador
        GPIO.setup(self.__noite, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Noche
        GPIO.setup(self.__dia, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Dia

    def encender_fuente(self):
        GPIO.output(self.__transformador_24v_pin, False)  # Encendemos Fuente
        time.sleep(1)

    def apagar_fuente(self):
        GPIO.output(self.__transformador_24v_pin, True)	# Desconectamos Fuente

    def abrir_porta(self):
        self._cadeado_porta.acquire()
        self.encender_fuente()
        GPIO.output(self.__motor_sentido2_pin, False)  # Alimentamos Motor (Sentido 2)
        time.sleep(self.__tempo_apertura_peche)
        GPIO.output(self.__motor_sentido2_pin, True)
        self._cadeado_porta.release()


    def pechar_porta(self):
        self._cadeado_porta.acquire()
        self.encender_fuente()
        GPIO.output(self.__motor_comun_pin, False) # Alimentamos - 0 V CC
        time.sleep(1)
        GPIO.output(self.__motor_sentido1_pin, False)  # Alimentamos Motor (Sentido 1)
        time.sleep(self.__tempo_apertura_peche)

        GPIO.output(self.__motor_sentido1_pin, True)  # Desconectamos Motor
        time.sleep(1)
        GPIO.output(self.__motor_comun_pin, True)  # Desconectamos -0V CC
        self._cadeado_porta.release()

    def e_dia(self):
        if not GPIO.input(self.__noite):
            return False
        elif not GPIO.input(self.__dia):
            return True

    def encender_incandescente(self):
        GPIO.output(self.__lampara_pin, False)  # Encender luz

    def apagar_incandescente(self):
        GPIO.output(self.__lampara_pin, True)  # Apagar luz

    def esta_pulsado(self):
        if not GPIO.input(20):
            time.sleep(0.2)
            while not GPIO.input(20):
                continue

            return True

        return False
