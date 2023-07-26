def menu():
    print("---- PLATAFORMA DE CONJUNTOS ----")
    print("Opções: ")
    print("1 - Criar conjunto")
    print("2 - Adicionar elemento")
    print("3 - Remover elemento")
    print("4 - Mostrar conjunto")
    opcao = input("> Escolha uma opção ou 's' para sair: ")
    return opcao

def criar_conjunto():
    return []

def mostrar_conjunto(id):
    print(lista_de_conjuntos[id-1])

def add_elemento(id, elemento):
    if id > len(lista_de_conjuntos):
        print("Conjunto inexistente")
    else:
        lista_de_conjuntos[id-1].append(elemento)

def del_elemento(id, elemento):
    if id > len(lista_de_conjuntos):
        print("Conjunto inexistente")
    else:    
        if elemento in lista_de_conjuntos[id-1]:
            lista_de_conjuntos[id-1].remove(elemento)    
        else:
            print("Elemento inexistente")


lista_de_conjuntos = []
while True:
    opcao = menu()
    if opcao in 'sS':
        break
    elif opcao == '1':
        lista_de_conjuntos.append(criar_conjunto())
        print(f"Conjunto {len(lista_de_conjuntos)} criado com sucesso!")
    elif opcao == '2':
        if len(lista_de_conjuntos) > 0:
            id_conjunto = int(input("> Digite o ID do conjunto que você quer adicionar: "))
            elemento = input("> Digite o elemento que você quer adicionar: ")
            add_elemento(id_conjunto, elemento)
        else:
            print("Operação inválida")
    elif opcao == '3':
        if len(lista_de_conjuntos) > 0:        
            id_conjunto = int(input("> Digite o ID do conjunto que você quer remover: "))
            elemento = input("> Digite o elemento que você quer remover: ")
            del_elemento(id_conjunto, elemento)      
        else:
            print("Operação inválida")              
    elif opcao == '4':
        if len(lista_de_conjuntos) > 0:        
            id_conjunto = int(input("> Digite o ID do conjunto que você quer ver: "))
            mostrar_conjunto(id_conjunto)
        else:
            print("Operação inválida")            