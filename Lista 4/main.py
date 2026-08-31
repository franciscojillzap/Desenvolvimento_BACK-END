from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/alunos/novo")
def formulario_aluno():
	return render_template("form_aluno.html")

# @app.route("/alunos/salvar", methods=["POST"])
def registrar_aluno():
	nome = request.form.get("nome")
	cpf = request.form.get("cpf")
	dt_nasc = request.form.get("data")
	email = request.form.get("e_mail")
	curso = request.form.get("curso")

	return render_template("sucesso.html")

##########################################################

# Formulário de Cadastro do Aluno
app.add_url_rule(rule="/alunos/novo", view_func=formulario_aluno, methods=["GET"])

# Resultado (de SUCESSO ou ERRO) do Cadastro
app.add_url_rule(rule="/alunos/salvar", view_func=registrar_aluno, methods=["POST"])

##########################################################

if __name__ == "__main__":
	app.run(debug=True)