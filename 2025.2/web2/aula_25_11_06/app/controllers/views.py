from flask import render_template, redirect, request, url_for
from app import app, db
from app.models.Pessoa import Pessoa

@app.route("/")
def index():
    pessoas_cadastradas = Pessoa.query.all() # SELECT * FROM Pessoa

    return render_template("index.html", pessoas=pessoas_cadastradas)

@app.route("/adicionar", methods=['POST'])
def adicionar():
    nome = request.form.get('nome') # pega (get) o atributo 'nome' do form que está no index

    if nome:
        nova_pessoa = Pessoa(nome=nome)
        db.session.add(nova_pessoa)
        db.session.commit()

    return redirect(url_for('index'))

@app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.get(id)

    db.session.delete(pessoa)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/editar/<int:id>", methods=['POST'])
def editar(id):
    pessoa = Pessoa.query.get(id)
    pessoa.nome = request.form.get('novo_nome')

    db.session.commit()

    return redirect(url_for('index'))