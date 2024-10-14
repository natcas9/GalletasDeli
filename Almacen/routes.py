from flask import Blueprint

bp = Blueprint('almacen', __name__)

@bp.route('/')
def index():
    return "Interfaz de Almacén"
