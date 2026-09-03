from flask import Flask, render_template, request

# @app.route("/")
def calculadora():
	return render_template("index.html")

# @app.route("/soma")
def somar():
	return render_template("form_soma.html")

# @app.route("/multiplicacao")
def multiplicar():
	return render_template("form_multiplicacao.html")

# @app.route("/resultado", methods=['GET', 'POST'])
def executar():
	soma = None
	multiplicacao = None

	if request.method == 'GET':
		# Recebe os valores entregues pelo formulário
		valor1 = request.values.get('n1')
		valor2 = request.values.get('n2')
		# Realiza a conversão dos valores para números INTEIROS
		num1 = int(valor1)
		num2 = int(valor2)
		# Efetua a SOMA
		resultado = num1 + num2
		# Comprova a operação utilizada
		operacao = "ADIÇÃO"

		# Dicionário que armazena os dados referentes a Soma
		soma = {
		'numero1': num1,
		'numero2': num2,
		'resultado': resultado,
		'operacao': operacao
		}

	elif request.method == 'POST':
		# Recebe os valores entregues pelo formulário
		valor1 = request.values.get('n1')
		valor2 = request.values.get('n2')
		# Realiza a conversão dos valores para números INTEIROS
		num1 = int(valor1)
		num2 = int(valor2)
		# Efetua a MULTIPLICAÇÃO
		resultado = num1 * num2
		# Comprova a operação utilizada
		operacao = "MULTIPLICAÇÃO"

		# Dicionário que armazena os dados referentes a Multiplicação
		multiplicacao = {
		'numero1': num1,
		'numero2': num2,
		'resultado': resultado,
		'operacao': operacao
		}

	contexto = {
	'soma': soma,
	'multiplicacao': multiplicacao
	}

	return render_template("resultado.html", **contexto)

# Reúne todas as rotas referentes a Calculadora
# Facilita a importação para o arquivo principal "main.py"
def rotas_calc(app):
	app.add_url_rule(rule="/", view_func=calculadora, methods=['GET'])
	app.add_url_rule(rule="/soma", view_func=somar, methods=['GET'])
	app.add_url_rule(rule="/multiplicacao", view_func=multiplicar, methods=['GET'])
	app.add_url_rule(rule="/resultado", view_func=executar, methods=['GET', 'POST'])