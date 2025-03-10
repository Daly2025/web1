from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template ('index.html')

@app.route('/saludo/<nombre>/<int:edad>')
def saludo(nombre,edad):
    if(edad<18):
        return 'Hola ' + nombre + "eres mayor de edad"
    else:
        return 'Hola ' + nombre + "eres menor de edad"
    
    #login post
@app.route('/login', methods=['POST'])
def login():
    #obtener datos del formulario
    username = request.form('username')
    password = request.form('password')
    return f"nombre: {username} pass: {password}"

if __name__ == '__main__':
    app.run(debug=True, port=80)