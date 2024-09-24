"""
Esta es la función de fábrica que crea la aplicación Flask. 
Configura la aplicación con los ajustes de la base de datos, 
inicializa SQLAlchemy y registra los blueprints de los módulos 
de Almacén y Ventas. 
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar base de datos
    db.init_app(app)
    
    # Registrar módulos
    from app.almacen import almacen_bp
    from app.ventas import ventas_bp

    app.register_blueprint(almacen_bp, url_prefix='/almacen')
    app.register_blueprint(ventas_bp, url_prefix='/ventas')

    return app
