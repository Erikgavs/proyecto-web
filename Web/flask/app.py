
from flask import Flask, render_template, request, redirect # RENDER TEMPLATE PERMITE LEER LOS ARCHIVOS DE LA PLANTILLA TEMPLATES

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

@app.route('/register')
def register():
     return render_template('register.html')

# FORMULARIO 
@app.route('/suscribirse', methods=['POST'])
def suscribirse():
    email = request.form.get('mail')
    numero = request.form.get('phone')
    print(f"Nuevo registro, Correo: {email} y telefono: {numero}")
    with open("suscriptores.txt", "a") as file:
        file.write(f"{email}, {numero}\n")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)