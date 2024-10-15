from flask import Flask
from routes import ventas_blueprint

def run_ventas_service():
    app = Flask(__name__)
    app.register_blueprint(ventas_blueprint)
    app.run(host="0.0.0.0", port=5002)  # Levanta el servicio de Ventas en el puerto 5002

if __name__ == "__main__":
    run_ventas_service()
