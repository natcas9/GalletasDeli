from flask import Flask
from routes import almacen_blueprint

def run_almacen_service():
    app = Flask(__name__)
    app.register_blueprint(almacen_blueprint)
    app.run(host="0.0.0.0", port=5001)  # Levanta el servicio de Almacén en el puerto 5001

if __name__ == "__main__":
    run_almacen_service()
