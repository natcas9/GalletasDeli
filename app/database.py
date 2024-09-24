"""
Este archivo inicializa una instancia de SQLAlchemy 
que manejará la conexión con la base de datos y la 
interacción con los modelos definidos en los módulos.

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()