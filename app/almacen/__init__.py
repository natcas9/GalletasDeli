"""
Este archivo crea un blueprint para 
el módulo de Almacén, lo que permite 
encapsular las rutas y funciones 
específicas de este módulo.

"""


from flask import Blueprint

almacen_bp = Blueprint('almacen', __name__)

from app.almacen import routes
