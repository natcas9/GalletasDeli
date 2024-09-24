"""
Estas son las rutas que manejan el módulo de Gestión de Almacén.

"""

from flask import jsonify, request
from app.almacen import almacen_bp
from app.database import db
from app.almacen.models import Almacen, Insumo

@almacen_bp.route('/inventario', methods=['GET'])
def inventario():
    inventario = Almacen.query.all()
    return jsonify([{'nombre': item.nombre, 'cantidad': item.cantidad, 'lote': item.lote} for item in inventario])

@almacen_bp.route('/add', methods=['POST'])
def add_inventario():
    data = request.get_json()
    nuevo_item = Almacen(nombre=data['nombre'], cantidad=data['cantidad'], lote=data['lote'])
    db.session.add(nuevo_item)
    db.session.commit()
    return jsonify({'message': 'Item agregado con éxito'}), 201
