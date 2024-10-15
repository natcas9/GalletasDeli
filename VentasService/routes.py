from flask import Blueprint, jsonify, request
from authentication import login, services_started, start_additional_services

ventas_blueprint = Blueprint('ventas', __name__)

@ventas_blueprint.route('/login', methods=['POST'])
def authenticate_user():
    return login()

# Ruta de prueba para ventas
@ventas_blueprint.route('/ventas', methods=['GET'])
def listar_ventas():
    if not services_started:
        return jsonify({"error": "Servicios de Almacén y Entregas no están activos."}), 403
    return jsonify({"ventas": "Aquí va la lista de ventas"})
