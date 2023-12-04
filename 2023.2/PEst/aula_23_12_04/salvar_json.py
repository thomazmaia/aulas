import json

pessoas = {
    'yasmim' : {
        'idade' : 16, 
        'hobby' : 'jogar volei'
        },
    'ana' : {
        'idade' : 18, 
        'hobby' : 'ler'
        },
    'ramon' : {
        'idade' : 18, 
        'hobby' : 'jogar xadrez'
        }
}

with open("nome_do_arquivo.json", "w") as f:
    json.dump(pessoas, f)