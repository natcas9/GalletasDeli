"""

Este es el archivo que se va a ejecutar para que la aplicación Flask se cree,
lo que va a hacer es iniciar en modo depuración la aplicación create_app(), inicializar
los módulos de registro y almacén

"""

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Ruta a la base de datos
db_path = os.path.join('Database', 'GalletasDeliDB.db')

# Clase User para Flask-Login
class User(UserMixin):
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

# Cargar usuario por ID
@login_manager.user_loader
def load_user(user_id):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Nombre, Email FROM Clientes WHERE ID = ?", (user_id,))
        user_data = cursor.fetchone()
    if user_data:
        return User(id=user_data[0], username=user_data[1], email=user_data[2])
    return None

# Página de inicio
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', username=current_user.username)
    return redirect(url_for('/LoginRegisterService/login.html'))

# Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID, Nombre, Email, Contraseña FROM Clientes WHERE Email = ?", (email,))
            user_data = cursor.fetchone()

        if user_data and check_password_hash(user_data[3], password):
            user = User(id=user_data[0], username=user_data[1], email=user_data[2])
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('index'))
        else:
            flash("Correo o contraseña incorrectos", "error")
    
    return render_template('/LoginRegisterService/login.html')

# Página de registro de usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['username']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Clientes (Nombre, Direccion, Telefono, Email, Contraseña) VALUES (?, ?, ?, ?, ?)",
                           (nombre, direccion, telefono, email, hashed_password))
            conn.commit()
            flash("Usuario registrado exitosamente. Por favor, inicia sesión.", "success")
            return redirect(url_for('login'))
    
    return render_template('/LoginRegisterService/register.html')

# Cerrar sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión exitosamente.", "success")
    return redirect(url_for('login'))

# Página protegida para usuarios autenticados
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)


#Pruebas de salida de ingredientes a produccion 
@app.route('/pagina-principal-salida')
def pagina_principal_salida():
    return render_template('salida-ingredientes1.html')

@app.route('/filtro')
def filtro():
    return render_template('salida-ingredientes2.html')

@app.route('/checkbox')
def checkbox():
    return render_template('salida-ingredientes3.html')

@app.route('/datos-operacion')
def datos_operacion():
    return render_template('salida-ingredientes4.html')

@app.route('/detalles-salida')
def detalles_salida():
    return render_template('salida-ingredientes5.html')

@app.route('/salida')
def salida():
    return render_template('salida-ingredientes6.html')



if __name__ == '__main__':
    app.run(debug=True)
