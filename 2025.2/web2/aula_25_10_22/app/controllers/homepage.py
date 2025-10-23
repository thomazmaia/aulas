from app import app
from flask import render_template


@app.route("/")
def olaMundo():
    nome = "Maria"
    return render_template("index.html", var=nome)