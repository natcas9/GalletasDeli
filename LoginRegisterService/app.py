from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Database/GalletasDeliDB.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

# Variable global para rastrear si ya se ejecutó la lógica inicial
first_request_done = False

@app.before_request
def before_first_request_logic():
    global first_request_done
    if not first_request_done:
        # Código que quieres que se ejecute antes de la primera solicitud
        print("Esto se ejecuta antes de procesar la primera solicitud.")
        # Ejemplo: Crear tablas si no existen
        db.create_all()
        first_request_done = True

# Modelo de ejemplo (asegúrate de que tu modelo esté bien definido en models.py)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de ejemplo para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica para manejo de login
        pass
    return render_template('login.html')

# Ruta de ejemplo para logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
