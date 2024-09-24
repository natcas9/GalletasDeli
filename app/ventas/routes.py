"""
Estas son las rutas que manejan el módulo de Gestión de Ventas.

"""


from flask import jsonify, request
from app.ventas import ventas_bp
from app.database import db
from app.ventas.models import Venta
from app.almacen.models import Almacen

@ventas_bp.route('/registrar', methods=['POST'])
def registrar_venta():
    data = request.get_json()
    
    # Registrar venta
    venta = Venta(cliente=data['cliente'], producto_id=data['producto_id'], cantidad=data['cantidad'])
    db.session.add(venta)

    # Ajustar inventario
    producto = Almacen.query.get(data['producto_id'])
    if producto:
        producto.cantidad -= data['cantidad']
        db.session.commit()
        return jsonify({'message': 'Venta registrada y inventario actualizado'}), 201
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404
