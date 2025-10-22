from app import app
from flask import render_template


@app.route("/")
def olaMundo():
    nome = "Xico"
    return render_template("index.html", nome=nome)