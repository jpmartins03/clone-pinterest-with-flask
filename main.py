from flask import Flask, render_template ##procura no projeto a pasta chamada templates e carrega os arquivos 

app = Flask(__name__) # estou criando meu aplicativo flask com o nome do arquivo que estou usando (no caso main)


# caminho do link do meu site

# rota da homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil")
def ProfilePage():
    return render_template("profilepage.html")


# coloca o site no ar, se eu executar o arquivo e ele retornar o nome dele mesmo,
# assim garanto que ele nao seja executado em imports, apenas nele mesmo
if __name__ == "__main__":
    app.run(debug=True)
