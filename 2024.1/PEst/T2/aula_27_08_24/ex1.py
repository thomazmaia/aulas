# Crie um programa que mantenha um banco de dados de filmes. Cada filme deve ter informações como título, diretor, ano de lançamento e gênero. Use listas aninhadas para armazenar os filmes, onde cada filme é uma lista com suas informações. O programa deve permitir adicionar filmes, pesquisar filmes por gênero e listar todos os filmes no banco de dados.

def escreve_menu():
    print("---------------------")
    print("1 - Adicionar filme")
    print("2 - Listar filmes")
    print("3 - Pesquisar filme por gênero")
    print("4 - Sair")
    opcao = int(input(">> Digite a opção: "))
    print("---------------------")
    return opcao


def adicionar_filme():
    titulo = input("Digite o título do filme: ")
    diretor = input("digite o nome do diretor: ")
    ano = input("Digite o ano de lançamento: ")
    genero = input("Digite o gênero do filme: ")
    filme = [titulo, diretor, ano, genero]
    banco_de_dados.append(filme)
    print(f"{titulo} adicionado com sucesso!")


def listar_filmes():
    for filme in banco_de_dados:
        # filme = [titulo, diretor, ano, genero]
        print(f"{filme[0]} ({filme[2]})")


def buscar_filme_por_genero():
    genero = input("Digite o gênero que está buscando: ")
    # filme = [titulo, diretor, ano, genero]
    for filme in banco_de_dados:
        if genero == filme[3]:
            print(f"{filme[0]} ({filme[2]})")


banco_de_dados = []
while True:
    op = escreve_menu()
    if op == 1:
        adicionar_filme()
    elif op == 2:
        listar_filmes()
    elif op == 3:
        buscar_filme_por_genero()
    elif op == 4:
        break
    else:
        print("Opcão inválida!")