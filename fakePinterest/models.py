## arquivo que cria a estrutura do banco de dados
from fakePinterest import database
from datetime import datetime

## preciso passar o parametro database.Model para que o python entenda que isso nao é um classe comum do python
## mas sim uma classe modelo para criar uma tabela no banco de dados
## o nome da tabela vai ser o nome da classe em minusculo, e o plural dela
## por exemplo, se eu criar a classe User, o nome da tabela vai ser user
## se eu criar a classe Post, o nome da tabela vai ser post
## se eu criar a classe Comment, o nome da tabela vai ser comment
class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    posts = database.relationship("Post", backref="user", lazy=True)
    # o backref cria uma relação entre as tabelas, assim posso acessar os posts de um usuário
    # e o lazy=True significa que os Sosts só serão carregados quando eu precisar

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.String, default="default.png")
    description = database.Column(database.String, nullable=False)
    create_at = database.Column(database.DateTime, default=datetime.utcnow)
    id_user = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
    # o ForignKey cria uma relação entre as tabelas, assim posso acessar o usuário
    # que criou o post, e o nullable=False significa que esse campo é obrigatório

