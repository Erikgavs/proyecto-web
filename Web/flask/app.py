
from flask import Flask, render_template, request, redirect, url_for # RENDER TEMPLATE PERMITE LEER LOS ARCHIVOS DE LA PLANTILLA TEMPLATES

app = Flask(__name__)

# SI EL VISITANTE PONE HTTPS://EXAMPLE.COM/  AUTOMÁTICAMENTE LE LLEVARÁ AL INDEX.HTML 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/register')
def register():
    return render_template('register.html')

@app.route('/login/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/login/privileges')
def privileges():
    return render_template('privileges.html')

# FORMULARIO INDEX.HTML
@app.route('/suscribirse', methods=['POST'])
def suscribirse():
    email = request.form.get('mail')
    numero = request.form.get('phone')
    print(f"Nuevo registro, Correo: {email} y telefono: {numero}")
    with open("suscriptores.txt", "a") as file:
        file.write(f"{email}, {numero}\n")
    return redirect('/')

#FORMULARIO LOGIN
@app.route('/runsesion', methods=['POST'])
def runsesion():
    email = request.form.get('email')
    contraseña = request.form.get('password')
    print(f'Nuevo inicio de sesión, correo {email} y contraseña {contraseña}')
    with open("inicios_sesión.txt", "a") as file:
        file.write(f"Correo: {email}, Contraseña: {contraseña}\n")
    return redirect('/login/privileges') # CAMBIAR ESTA LÍNEA CUANDO LAS NUEVAS PÁGINAS ESTÉN CREADAS

#FORMULARIO REGISTER
@app.route('/createsesion', methods=['POST'])
def createsesion():
    email = request.form.get('email')
    contraseña = request.form.get('password1')
    print(f'Creación de cuenta completada, correo: {email}, contraseña: {contraseña}')
    with open("creacion_cuenta.txt", "a") as file:
        file.write(f"Correo: {email}, contraseña: {contraseña}\n")
    return redirect('/')

#FORMULARIO FORGOT PASSWORD
#MAÑANA COMPROBAR SI FUNCIONA
@app.route('/backup', methods=['POST'])
def backup():
    email = request.form.get('email')
    with open("ebackup.txt", "a") as file:
        file.write(f"Correo para recuperar contraseña: {email}\n")
    return redirect('/')

# ARREGLAR LOS REDIRECTS



if __name__ == '__main__':
    app.run(debug=True)