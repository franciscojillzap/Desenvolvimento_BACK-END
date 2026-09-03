from flask import Flask

# Importa do arquivo "calculadora.py", dentro da pasta "routes", a função "rotas_calc"
from routes.calculadora import rotas_calc

app = Flask(__name__)

rotas_calc(app)

if __name__ == '__main__':
	app.run(debug=True)