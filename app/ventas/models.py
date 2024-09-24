"""
Este archivo define los modelos de la base 
de datos relacionados con las venats.

Se pueden definir las columnas y las bases 
de datos directamente desde esta aplicación

"""

from app.database import db
from app.almacen.models import Almacen  # Relación con Almacén

class Venta(db.Model):
    __tablename__ = 'venta'
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('almacen.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    producto = db.relationship('Almacen')
