"""

Este es el archivo que se va a ejecutar para que la aplicación Flask se cree,
lo que va a hacer es iniciar en modo depuración la aplicación create_app(), inicializar
los módulos de registro y almacén

"""

from flask import Flask
from Almacen import routes as almacen_routes
from Ventas import routes as ventas_routes

app = Flask(__name__)

# Configuración específica para cada módulo
app.config.from_pyfile('Config_almacen.py')
app.config.from_pyfile('Config_ventas.py')

# Registro de los blueprints de cada módulo
app.register_blueprint(almacen_routes.bp, url_prefix='/almacen')
app.register_blueprint(ventas_routes.bp, url_prefix='/ventas')

if __name__ == '__main__':
    app.run(debug=True)
