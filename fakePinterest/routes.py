# Arquivo: fakePinterest/routes.py

# A primeira coisa é importar o 'app' que foi criado no __init__.py
from fakePinterest import app
from flask import render_template
from flask_login import login_required

#importa os formularios do meu arquivo
from fakePinterest.forms import FormLogin, FormCriarConta

# rota da homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form = formlogin)

idade = 21
# a tag < > diz que é uma variavel

@app.route("/criar_conta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form = formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def ProfilePage(usuario):
    return render_template("profilepage.html", usuario=usuario, idade=idade)