from dotenv import load_dotenv
from src.controllers import CoreGalineiro
from src.app import app
import threading
import os

if __name__ == '__main__':
    load_dotenv()

    CoreGalineiro.instance().root_path = os.path.dirname(
                                            os.path.abspath(__file__))
    ciclo_thread = threading.Thread(target=CoreGalineiro.instance().ciclo)
    ciclo_thread.start()

    ciclo_thread_mobil = threading.Thread(
        target=CoreGalineiro.instance().comprobacion_estado_manual_mobil)
    ciclo_thread_mobil.start()
    app.run(threaded=True, use_reloader=False)
