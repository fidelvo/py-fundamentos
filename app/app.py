from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
  print('Antes de la petición...')

@app.after_request
def after_request(response):
  print('Después de la petición...')
  return response

# Rutas
@app.route('/holamundo')
def hola_mundo():
  return "Hola Mundo"

def index():
  print('Estamos realizando la petición...')
  data = {
    'titulo' : 'Inicio',
    'contenido' : 'Página de Inicio'
  }
  return render_template('index.html', data = data)

@app.route('/contacto')
def contacto():
  data = {
    'titulo' : 'Contacto',
    'contenido' : 'Página de Contacto'
  }
  return render_template('contacto.html', data = data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
  return '¡Hola, {0}!'.format(nombre)

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
  return 'El resultado es: {0}'.format((valor1 + valor2))

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
  return 'Tu nombre es: {0} y tu edad es: {1}'.format(nombre, edad)

@app.route('/lenguajes')
def lenguajes():
  data = {
    'lenguajes' : ['PHP', 'Python', 'Kotlin', 'Swift', 'Java', 'C#', 'Javascript']
  }
  return render_template('lenguajes.html', data = data)

  # HTTP:
  # GET, POST, PUT, PATCH, DELETE

@app.route('/datos')
def datos():
  # print(request.args)
  v1 = request.args.get('valor1')
  v2 = int(request.args.get('valor2'))
  return 'Estos son los datos: {0}, {1}'.format(v1, (v2 + 10))

if __name__ == '__main__':
  app.add_url_rule('/', view_func=index)
  app.run(debug=True, port=5005)