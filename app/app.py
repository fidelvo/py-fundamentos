from flask import Flask

app = Flask(__name__)

# Rutas
def index():
  return "Página de inicio"

@app.route('/holamundo')
def hola_mundo():
  return "Hola Mundo"

if __name__ == '__main__':
  app.add_url_rule('/', view_func=index)
  app.run(debug=True, port=5005)