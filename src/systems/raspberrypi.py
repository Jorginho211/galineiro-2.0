from .base import SystemBase
import time
import RPi.GPIO as GPIO

class RaspberryPi(SystemBase):
    def __init__(self):
        super().__init__()

        self.__lampara_pin = 7              # Lampara Incandescente Cortello
        self.__transformador_24v_pin = 15   # Alimentación Transformado 24 V CC
        self.__motor_comun_pin = 18         # - 0 V CC Motor Puerta
        self.__motor_sentido1_pin = 23      # + 24 V CC Motor Puerta (SEMTIDO 1)
        self.__motor_sentido2_pin = 24      # + 24 V CC Motor Puerta (Sentido 2)
        self.__luz_pulsador_pin = 25        # Luz Pulsador MAN/AUTO

        self.__pulsador_pin = 20            # Entrada de pulsador
        self.__noite_pin = 16               # Entrada para indicar se e noite
        self.__dia_pin = 12                 # Entrada para indicar se e dia

        self.__tempo_apertura_peche = 22    # Duracion da maniobra da porta

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
        GPIO.setup(self.__luz_pulsador_pin, GPIO.OUT)
        GPIO.output(self.__luz_pulsador_pin, True)

        # Configuracion entradas
        GPIO.setup(self.__pulsador_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pulsador
        GPIO.setup(self.__noite_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Noche
        GPIO.setup(self.__dia_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Dia

    def encender_fuente(self):
        GPIO.output(self.__transformador_24v_pin, False)  # Encendemos Fuente
        time.sleep(1)

    def apagar_fuente(self):
        GPIO.output(self.__transformador_24v_pin, True)	# Desconectamos Fuente

    def abrir_porta(self):
        self._cadeado_porta.acquire()
        GPIO.output(self.__motor_sentido2_pin, False)  # Alimentamos Motor (Sentido 2)
        time.sleep(self.__tempo_apertura_peche)
        GPIO.output(self.__motor_sentido2_pin, True)
        self._cadeado_porta.release()


    def pechar_porta(self):
        self._cadeado_porta.acquire()
        GPIO.output(self.__motor_comun_pin, False) # Alimentamos - 0 V CC
        time.sleep(1)
        GPIO.output(self.__motor_sentido1_pin, False)  # Alimentamos Motor (Sentido 1)
        time.sleep(self.__tempo_apertura_peche)

        GPIO.output(self.__motor_sentido1_pin, True)  # Desconectamos Motor
        time.sleep(1)
        GPIO.output(self.__motor_comun_pin, True)  # Desconectamos -0V CC
        self._cadeado_porta.release()

    def e_dia(self):
        if not GPIO.input(self.__noite_pin):
            return False
        elif not GPIO.input(self.__dia_pin):
            return True

    def encender_incandescente(self):
        GPIO.output(self.__lampara_pin, False)  # Encender luz

    def apagar_incandescente(self):
        GPIO.output(self.__lampara_pin, True)  # Apagar luz

    def encender_luz_pulsador(self):
        self.encender_fuente()
        GPIO.output(self.__luz_pulsador_pin, False)

    def apagar_luz_pulsador(self):
        self.apagar_fuente()
        GPIO.output(self.__luz_pulsador_pin, True)

    def esta_pulsado(self):
        ret = False

        if not GPIO.input(self.__pulsador_pin):
            time.sleep(0.2)
            if not GPIO.input(self.__pulsador_pin):
                ret = True

            while not GPIO.input(self.__pulsador_pin):
                continue

        return ret
