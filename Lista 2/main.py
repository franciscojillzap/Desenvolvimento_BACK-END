from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
def boas_vindas():
	return render_template("boas_vindas.html")

# @app.route("/saudacao/<usuario>")
def saudacoes(usuario):
	return render_template("saudacao.html", nome=usuario)

# @app.route("/cadastro")
def formulario():
	return render_template("cadastro.html")

# @app.route("/resultado", methods=['POST'])
def exibir_resultado():
	nome = request.form.get("nome_user")
	idade = request.form.get("idade_user")
	curso = request.form.get("curso_user")

	return render_template("resultado_cadastro.html", name=nome, age=idade, course=curso)

###################################################################

# Boas Vindas
app.add_url_rule(rule="/", view_func=boas_vindas, methods=["GET"])

# Saudação Personalizada
app.add_url_rule(rule="/saudacao/<usuario>", view_func=saudacoes, methods=["GET"])

# Formulário de Cadastro
app.add_url_rule(rule="/cadastro", view_func=formulario, methods=["GET"])

# Resultados do Cadastro
app.add_url_rule(rule="/resultado", view_func=exibir_resultado, methods=["POST"])

###################################################################

if __name__ == "__main__":
	app.run(debug=True)
