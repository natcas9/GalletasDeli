"""

Este es el archivo que se va a ejecutar para que la aplicación Flask se cree,
lo que va a hacer es iniciar en modo depuración la aplicación create_app(), inicializar
los módulos de registro y almacén

"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)