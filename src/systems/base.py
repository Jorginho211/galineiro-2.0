from threading import Lock

class SystemBase:
    def __init__(self):
        self._cadeado_porta = Lock()

    def encender_fuente(self):
        raise Exception("not implemented")

    def apagar_fuente(self):
        raise Exception("not implemented")

    def abrir_porta(self):
        raise Exception("not implemented")

    def pechar_porta(self):
        raise Exception("not implemented")

    def e_dia(self):
        raise Exception("not implemented")

    def encender_incandescente(self):
        raise Exception("not implemented")

    def apagar_incandescente(self):
        raise Exception("not implemented")

    def encender_luz_pulsador(self):
        raise Exception("not implemented")

    def apagar_luz_pulsador(self):
        raise Exception("not implemented")

    def esta_pulsado(self):
        raise Exception("not implemented")
