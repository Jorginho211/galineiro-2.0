from src import app
from src.controllers import CoreGalineiro
import os

if __name__ == '__main__':
    CoreGalineiro.instance().root_path = os.path.dirname(os.path.abspath(__file__))
    app.run(threaded=True)
