"""
Este archivo define los modelos de la base 
de datos relacionados con el almacén.

Se pueden definir las columnas y las bases 
de datos directamente desde esta aplicación

"""

from app.database import db

class Almacen(db.Model):
    __tablename__ = 'almacen'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    lote = db.Column(db.String(50), nullable=False)

class Insumo(db.Model):
    __tablename__ = 'insumo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    lote = db.Column(db.String(50), nullable=False)
