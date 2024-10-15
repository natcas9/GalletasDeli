from flask import Flask
from routes import entregas_blueprint

def run_entregas_service():
    app = Flask(__name__)
    app.register_blueprint(entregas_blueprint)
    app.run(host="0.0.0.0", port=5003)  # Levanta el servicio de Entregas en el puerto 5003

if __name__ == "__main__":
    run_entregas_service()
