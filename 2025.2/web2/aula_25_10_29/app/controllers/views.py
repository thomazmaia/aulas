from app import app
from flask import render_template, request

@app.route("/saudacao")
def saudacao():
    nome = request.args.get('nome') # pega o valor enviado pela URL (?nome=Fulano)
    if nome:
        return render_template('saudacao.html', nome=nome)
    
    return render_template('saudacao.html', nome=None)


@app.route("/mensagem", methods=['GET', 'POST'])
def mensagem():
    if request.method == 'POST':
        nome = request.form.get('nome')
        mensagem = request.form.get('mensagem')
        return render_template('mensagem.html', nome=nome, mensagem=mensagem)
    
    return render_template('mensagem.html', nome=None, mensagem=None)