from flask import Flask
from routers.calculadora import rotas_calculadora

app = Flask(__name__)

rotas_calculadora(app)

if __name__ == '__main__':
    app.run(debug=True)