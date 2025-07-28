## arquivo que roda o projeto
from fakePinterest import app

# coloca o site no ar, se eu executar o arquivo e ele retornar o nome dele mesmo,
# assim garanto que ele nao seja executado em imports, apenas nele mesmo
if __name__ == "__main__":
    app.run(debug=True)
 