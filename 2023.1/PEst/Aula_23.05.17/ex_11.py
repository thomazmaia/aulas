import json


def menu():
    print("------------------------------")
    print("1 - Adicionar produto")
    print("2 - Atualizar preço de produto")
    print("3 - Apagar produto")
    print("4 - Mostrar produtos")
    print("5 - Salvar produtos")
    print("6 - Carregar produtos")
    print("------------------------------")
    op = int(input("Digite a opção: "))
    return op


def adicionar_novo_produto(produto, categoria, preco):
    produtos[produto] = {"categoria": categoria, "preco": preco}


def atualizar_preco():
    produto = input("Digite o nome do produto: ")
    novo_preco = float(input(f"Digite o novo preço do {produto}: "))
    produtos[produto]["preco"] = novo_preco


def mostrar_produtos():
    print("------ Produtos:")
    for chave, valor in produtos.items():
        print(chave, valor["categoria"], valor["preco"])


def salvar_dicionario(dicionario):
    with open("meus_produtos.json", "w") as f:
        json.dump(dicionario, f)


def carregar_dicionario(nome):
    with open(nome, "r") as f:
        dic = json.load(f)
    return dic


produtos = {}

while True:
    op = menu()
    if op == 1:
        produto = input("Digite o nome do produto: ")
        categoria = input(f"Digite a categoria do {produto}: ")
        preco = float(input(f"Digite o preço do {produto}: "))
        adicionar_novo_produto(produto, categoria, preco)
    elif op == 2:
        atualizar_preco()
    elif op == 3:
        produto = input("Digite o nome do produto: ")
        del produtos[produto]
    elif op == 4:
        mostrar_produtos()
    elif op == 5:
        salvar_dicionario(produtos)
    elif op == 6:
        path = input("Digite o nome do arquivo: ")
        produtos = carregar_dicionario(path)
    else:
        break
