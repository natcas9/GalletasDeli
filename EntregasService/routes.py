from flask import Blueprint, jsonify

entregas_blueprint = Blueprint('entregas', __name__)

@entregas_blueprint.route('/entregas', methods=['GET'])
def listar_entregas():
    # Aquí va la lógica para obtener las entregas (puedes conectar con una base de datos)
    return jsonify({"entregas": "Lista de entregas"})
