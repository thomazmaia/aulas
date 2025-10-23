from app import app
from flask import render_template


@app.route("/")
def olaMundo():
    nome1 = "Maria"
    nome2 = "Xico"
    return render_template("index.html", var1=nome1, var2=nome2)