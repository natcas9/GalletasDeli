import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('GalletasDeli.db')
cursor = conn.cursor()

#Ejemplo de como crear una tabla con relación
"""
# Crear la tabla 'Teams'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams (
        Team_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Team_name TEXT NOT NULL,
        Team_initials TEXT
    )
''')
"""

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tablas creadas exitosamente.")
