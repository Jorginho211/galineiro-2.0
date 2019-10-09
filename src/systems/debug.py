from .base import SystemBase

class Debug(SystemBase):
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
        return True

    def encender_incandescente(self):
        print("encendido")

    def apagar_incandescente(self):
        print("apagado")

    def esta_pulsado(self):
        return False