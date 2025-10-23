from app import app
from flask import render_template


@app.route("/")
def olaMundo():
    nome1 = "Maria"
    nome2 = "Xico"
    return render_template("index.html", var1=nome1, var2=nome2)


@app.route("/frutas")
def minhas_frutas():
    lista = ["uva", "maçã", "abacaxi", "limão"]
    return render_template("frutas.html", lista=lista)

@app.route("/contato")
def contato():
    pessoa = {
        "nome" : "Francisco José da Silva",
        "idade" : 62,
        "ocupacao" : "aposentado"
    }
    return render_template("contato.html", user=pessoa)

