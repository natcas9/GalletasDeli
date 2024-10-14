from flask import Blueprint

bp = Blueprint('ventas', __name__)

@bp.route('/')
def index():
    return "Interfaz de Ventas"
