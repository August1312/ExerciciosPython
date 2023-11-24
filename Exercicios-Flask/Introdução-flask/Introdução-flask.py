from flask import Flask

app = Flask(__name__)


@app.route("/") ####route -> eo caminho depois do dominio ####
def homepage():   ####função -> e oque você quer exibir naquela página #### 
    return "Hello world "

@app.route("/contatos")
def contatos():
    return "Contatos"



##### Colocar o site no ar ######
if __name__ == "__main__":
    app.run(debug=True) #### debug=treu Atualiza automaticamente o site sem precisa fica rodando toda hora. 