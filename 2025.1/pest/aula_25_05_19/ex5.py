# Crie um programa que ajude o usuário a gerenciar uma lista de compras. O programa deve permitir que o usuário adicione itens à lista, remova itens existentes, e exiba a lista de compras atual. Certifique-se de usar os métodos de lista apropriados para adicionar, remover e verificar a existência de itens na lista.

def menu():
    print("----------------")
    print("     MENU       ")
    print("----------------")
    print("[0] Sair")
    print("[1] Ver lista de compras")
    print("[2] Adicionar à lista de compras")
    print("[3] Remover da lista de compras")
    print("----------------")


def mostrar_lista():
    for item in lista_de_compras:
        print(item)

lista_de_compras = []

opcao = -1
while opcao != 0:
    menu()
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        mostrar_lista()
    elif opcao == 2:
        produto = input("Digite o produto que quer adicionar: ")
        lista_de_compras.append(produto)
    elif opcao == 3:
        produto = input("Digite o produto que quer remover: ")
        if produto in lista_de_compras:
            lista_de_compras.remove(produto)