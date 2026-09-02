from flask import Flask, render_template

# @app.route("/")
def calculadora():
    return render_template("index.html")

# @app.route("/soma")
def somar():
    return render_template("form_soma.html")

# @app.route("/multiplicacao")
def multiplicar():
    return render_template("form_multiplicacao.html")

# @app.route("/resultado")
def executar():
    return render_template("resultado.html")

def rotas_calculadora(app):
    app.add_url_rule(rule="/", view_func=calculadora, methods=['GET'])
    app.add_url_rule(rule="/soma", view_func=somar, methods=['GET'])
    app.add_url_rule(rule="/multiplicacao", view_func=multiplicar, methods=['GET'])
    app.add_url_rule(rule="/resultado", view_func=executar, methods=['GET', 'POST'])