# ['Nome do Aluno]', 10, 10, 10, 10, 10]

def menu():
    print("------------------------")
    print("Escolha uma opção abaixo")
    print(" 0 - SAIR")
    print(" 1 - Adicionar")
    print(" 2 - Mostrar")
    print(" 3 - Modificar")
    print(" 4 - Apagar")
    print("------------------------")
    opcao = int(input("Opção: "))
    return opcao

def add():
    if len(cadastro) == 0:
        nome = input("Digite o nome do aluno: ")
        cadastro.append(nome)
        for i in range(5):
            nota = float(input(f"Digite a {i+1}a nota do {nome}: "))
            cadastro.append(nota)
        print(f"{nome} cadastrado com sucesso!")            
    else:
        print("[ERRO] Já existe usuário cadastrado.")


def deletar():
    tamanho = len(cadastro)
    for i in range(tamanho):
        cadastro.pop()
    print("Usuário apagado com sucesso")


def modificar() :
    print(cadastro)
    i = int(input("Digite o índice do que você quer modificar: "))
    coisa = input("Digite o novo valor: ")
    cadastro[i] = coisa


cadastro = []

while True: 
    opcao = menu()
    if opcao < 0 or opcao > 4:
        print("Opção inválida. Tente novamente.")    
    elif opcao == 0:
        break
    elif opcao == 1:
        add()
    elif opcao == 2:
        print(cadastro)
    elif opcao == 3:
        modificar()
    elif opcao == 4:
        deletar()