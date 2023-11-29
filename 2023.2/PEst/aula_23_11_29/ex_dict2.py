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

nome = input("Digite o nome: ").lower()

if nome in pessoas.keys():
    print(pessoas[nome]['hobby'])
else:
    print("Essa pessoa não está cadastrada. Vamos cadastrar.")
    nova_pessoa = dict()
    nova_pessoa['idade'] = input("Digite a idade: ")
    nova_pessoa['hobby'] = input("Digite o hobby: ")
    pessoas[nome] = nova_pessoa

for k,v in pessoas.items():
    print(f"{k} : {v}")
