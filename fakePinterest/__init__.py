# Arquivo: fakePinterest/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "2db9afb44d153b25f994b0cdbe01652e"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


# A importação das rotas e outros módulos do seu projeto
# deve vir DEPOIS da definição do 'app'.
# Isso evita o erro de importação circular.
from fakePinterest import routes
# Você pode descomentar as linhas abaixo quando for usar os arquivos
# from fakePinterest import models
# from fakePinterest import forms