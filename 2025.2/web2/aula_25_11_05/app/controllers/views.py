from app import app, db
from flask import render_template, redirect, url_for, request
from app.models import Usuario

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.Usuario.query.all() # SELECT * FROM usuario
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    idade = int(request.form.get('idade'))

    if nome and idade:
        novo = Usuario.Usuario(nome=nome, idade=int(idade))
        db.session.add(novo)
        db.session.commit()

    return redirect(url_for('listar_usuarios'))