# Arquivo: fakePinterest/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
database = SQLAlchemy(app)

# A importação das rotas e outros módulos do seu projeto
# deve vir DEPOIS da definição do 'app'.
# Isso evita o erro de importação circular.
from fakePinterest import routes
# Você pode descomentar as linhas abaixo quando for usar os arquivos
# from fakePinterest import models
# from fakePinterest import forms