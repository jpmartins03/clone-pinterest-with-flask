## para criar o banco preciso importar la do init, o app e o database
from fakePinterest import database, app
from fakePinterest.models import User, Post


##preciso definir que estou "olhando" para meu app e dentro do contexto dele estou criando meu banco de dados

with app.app_context():
    database.create_all()
# Agora o banco de dados foi criado e está pronto para uso.
# se eu rodar esse arquivo, ele vai criar o banco de dados
# e as tabelas definidas nos modelos (models) que você criar.