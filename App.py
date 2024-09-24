import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
# from functions import Config
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generar una clave secreta segura

# Simulamos una base de datos con productos
productos = [
    {'id': 1, 'nombre': 'Producto A', 'precio': 10.0},
    {'id': 2, 'nombre': 'Producto B', 'precio': 20.0},
    {'id': 3, 'nombre': 'Producto C', 'precio': 30.0},
]

ventas = []

# Ruta principal para mostrar la interfaz de ventas
@app.route("/")
def home():
    return render_template("ventas.html")

# Ruta para procesar una venta
@app.route('/venta', methods=['POST'])
def procesar_venta():
    data = request.get_json()
    producto_id = data.get('producto_id')
    cantidad = data.get('cantidad')

    # Buscar el producto
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        total = producto['precio'] * cantidad
        ventas.append({
            'producto': producto['nombre'],
            'cantidad': cantidad,
            'total': total
        })
        return jsonify({'status': 'success', 'total': total})
    else:
        return jsonify({'status': 'error', 'message': 'Producto no encontrado'}), 404

# Ruta para ver las ventas
@app.route('/ventas', methods=['GET'])
def listar_ventas():
    return jsonify(ventas)

if __name__ == '__main__':
    app.run(debug=True)
