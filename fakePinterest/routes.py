# Arquivo: fakePinterest/routes.py

# A primeira coisa é importar o 'app' que foi criado no __init__.py
from fakePinterest import app
from flask import render_template
from flask_login import login_required

# rota da homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

idade = 21
# a tag < > diz que é uma variavel

@app.route("/perfil/<usuario>")
@login_required
def ProfilePage(usuario):
    return render_template("profilepage.html", usuario=usuario, idade=idade)