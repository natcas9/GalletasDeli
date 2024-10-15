from flask import jsonify, request
from multiprocessing import Process
from AlmacenService.app import run_almacen_service
from EntregasService.app import run_entregas_service
import time

# Simulación de usuarios con permisos
USERS = {
    "admin": {"password": "admin123", "role": "employee"},
    "cliente": {"password": "cliente123", "role": "client"}
}

# Variable para almacenar si los servicios ya se iniciaron
services_started = False

def login():
    global services_started
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = USERS.get(username)
    if user and user["password"] == password:
        if user["role"] == "employee":
            if not services_started:
                services_started = True
                start_additional_services()
            return jsonify({"message": "Inicio de sesión exitoso, servicios autorizados"}), 200
        else:
            return jsonify({"message": "Usuario autenticado pero no tiene permisos de empleado"}), 403
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401

def start_additional_services():
    print("Iniciando servicios de Almacén y Entregas...")
    
    # Crear procesos para Almacén y Entregas
    almacen_process = Process(target=run_almacen_service)
    entregas_process = Process(target=run_entregas_service)
    
    # Iniciar procesos
    almacen_process.start()
    entregas_process.start()
