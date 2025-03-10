from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/hola')
def index():
    return "¡Hola desde Flask!"

@app.route('/hello')
def hello_world():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
