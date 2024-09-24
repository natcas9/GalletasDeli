"""

Este es el archivo de configuración de la aplicación. 
Se define la URI de la base de datos con la opción de 
utilizar una variable de entorno en la cual se le pasa como
parametro una URL de la base a utilizar o una base de datos
SQLite por defecto.

También se desactiva el rastreo de modificaciones de SQLAlchemy para mejorar el rendimiento.

"""

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
