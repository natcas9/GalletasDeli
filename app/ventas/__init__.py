"""
Este archivo define el blueprint del módulo 
de Ventas, de forma similar al módulo de Almacén. 
Este blueprint encapsula todas las rutas y 
funcionalidades relacionadas con la gestión de ventas.

"""

from flask import Blueprint

ventas_bp = Blueprint('ventas', __name__)

from app.ventas import routes
