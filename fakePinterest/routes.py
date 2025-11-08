# Arquivo: fakePinterest/routes.py

# A primeira coisa é importar o 'app' que foi criado no __init__.py
from fakePinterest import app, database, bcrypt
from fakePinterest.models import User, Post
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

#importa os formularios do meu arquivo
from fakePinterest.forms import FormLogin, FormCriarConta

# rota da homepage
@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = User.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, formlogin.password.data):
            login_user(usuario)
            return redirect(url_for("ProfilePage", usuario=usuario.username))
                
    return render_template("homepage.html", form = formlogin)

idade = 21
# a tag < > diz que é uma variavel

@app.route("/criar_conta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        encryptedPassword = bcrypt.generate_password_hash(formcriarconta.password.data)
        # bcrypt.check_password_hash() 
        newUser = User(
            username=formcriarconta.username.data,
            email=formcriarconta.email.data,
            password=encryptedPassword,
            )
        database.session.add(newUser)
        database.session.commit()
        login_user(newUser, remember=True)
        return redirect(url_for("ProfilePage", usuario=newUser.username))
    return render_template("criarconta.html", form = formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def ProfilePage(usuario):
    return render_template("profilepage.html", usuario=usuario, idade=idade)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))
