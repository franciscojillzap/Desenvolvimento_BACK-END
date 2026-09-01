from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

# @app.route("/alunos/novo")
def formulario_aluno():
	return render_template("form_aluno.html")

# @app.route("/alunos/salvar", methods=["POST"])
def registrar_aluno():
	# Lista contendo todos os erros cometidos pelo usuário
	erros = []
	# Exibe uma mensagem de sucesso caso não haja dados dentro da lista de erros
	sucesso = None
	# Dicionário contendo todas as informações do aluno
	aluno = {}

	if request.method == "POST":
		aluno = {
		'nome': request.form.get("nome").strip(),
		'cpf': request.form.get("cpf").strip(),
		'dt_nasc': request.form.get("data"),
		'email': request.form.get("e_mail"),
		'curso': request.form.get("curso")
		}

	#### Validar NOME ####

	#Divide o texto em partes menores usando, por padrão, os espaços entre as palavras
	partes_nome = aluno['nome'].split()

	if not aluno['nome']:
		erros.append("O nome não pode ser composto apenas por espaços.")
	else:
		if len(partes_nome) < 2:
			erros.append("Deve possuir pelo menos NOME e SOBRENOME.")
		if any(char.isdigit() for char in aluno['nome']):
			erros.append("O nome não deve conter números.")

	#### Validar CPF ####

	if len(aluno['cpf']) < 11:
		erros.append("O CPF deve conter 11 dígitos númericos.")

	#### Validar DATA de NASCIMENTO ####

	data_atual = date.today()
	# Transforma a data em formato de texto (string) em uma data reconhecida pelo Python
	data_nasc_convertida = datetime.strptime(aluno['dt_nasc'], "%Y-%m-%d").date()

	if data_nasc_convertida > data_atual:
		erros.append("A data de nascimento não pode representar uma data futura.")
	else:
		idade = data_atual.year - data_nasc_convertida.year

		if idade < 14:
			erros.append("O aluno deve possuir idade mínima de 14 anos.")

	if not erros:
		sucesso = "Cadastro realizado com sucesso!"

	context = {
	"sucesso": sucesso,
	"erros": erros,
	"aluno": aluno
	}

	return render_template("sucesso.html", **context)

##########################################################

# Formulário de Cadastro do Aluno
app.add_url_rule(rule="/alunos/novo", view_func=formulario_aluno, methods=["GET"])

# Resultado (de SUCESSO ou ERRO) do Cadastro
app.add_url_rule(rule="/alunos/salvar", view_func=registrar_aluno, methods=["POST"])

##########################################################

if __name__ == "__main__":
	app.run(debug=True)