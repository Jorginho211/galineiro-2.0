from src.controllers import CoreGalineiro
from src.app import app
import threading
import os

if __name__ == '__main__':
    CoreGalineiro.instance().root_path = os.path.dirname(os.path.abspath(__file__))
    ciclo_thread = threading.Thread(target=CoreGalineiro.instance().ciclo)
    ciclo_thread.start()
    app.run(threaded=True)
