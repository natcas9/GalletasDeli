from flask import Blueprint, jsonify

almacen_blueprint = Blueprint('almacen', __name__)

@almacen_blueprint.route('/inventario', methods=['GET'])
def obtener_inventario():
    # Aquí va la lógica para obtener el inventario (puedes conectar con una base de datos)
    return jsonify({"inventario": "Lista de inventario disponible"})
