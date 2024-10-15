"""

Este es el archivo que se va a ejecutar para que la aplicación Flask se cree,
lo que va a hacer es iniciar en modo depuración la aplicación create_app(), inicializar
los módulos de registro y almacén

"""

from multiprocessing import Process
from VentasService.app import run_ventas_service
from AlmacenService.app import run_almacen_service
from EntregasService.app import run_entregas_service
import time

def run_all_services():
    # Levantar primero el servicio de Ventas
    ventas_process = Process(target=run_ventas_service)
    ventas_process.start()

    # Esperar unos segundos antes de levantar los otros servicios
    ventas_process.join()  # El servicio de Ventas requiere autenticación antes de los otros

if __name__ == "__main__":
    print("Iniciando el servicio de Ventas primero...")
    run_all_services()

