# Crie um programa que mantenha um banco de dados de filmes. Cada filme deve ter informações como título, diretor, ano de lançamento e gênero. Use listas aninhadas para armazenar os filmes, onde cada filme é uma lista com suas informações. O programa deve permitir adicionar filmes, pesquisar filmes por gênero e listar todos os filmes no banco de dados.

def escreve_menu():
    print("---------------------------------")
    print("[1] - Adicionar filme")
    print("[2] - Pesquisar filme por gênero")
    print("[3] - Listar filmes")
    print("[4] - Sair")
    opcao = int(input(">> Digite a opção: "))
    print("---------------------------------")    
    return opcao

def adicionar_filme():
    titulo = input("Digite o título: ")
    diretor = input("Digite o nome do diretor: ")
    ano = input("Digite o ano: ")
    genero = input("Digite o gênero: ")
    filme = [titulo, diretor, ano, genero]
    banco_de_filmes.append(filme)
    print(f"{titulo} adicionado com sucesso!!")

def pesquisar_filme_por_genero():
    genero = input("Digite o gênero a ser pesquisado: ")
    print(f"Mostrando filmes de {genero}:")
    for filme in banco_de_filmes:
        if filme[3] == genero:
            print(f"- {filme[0]} - ({filme[2]})")

def listar_filmes():
    print("Listando filmes...")
    for filme in banco_de_filmes:
        print(f"- {filme[0]} ({filme[2]})")
        


banco_de_filmes = []
while True:
    op = escreve_menu()
    if op == 1:
        adicionar_filme()
    elif op == 2:
        pesquisar_filme_por_genero()
    elif op == 3:
        listar_filmes()
    elif op == 4:
        break