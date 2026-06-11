# ['Bryan', 5.5, 6, 7, 4, 8]

def menu():
    print("----------------")
    print("Escolha a opção:")
    print("0 - Sair")
    print("1 - Cadastrar (C)")
    print("2 - Mostrar   (R)")
    print("3 - Atualizar (U)")
    print("4 - Deletar   (D)")
    print("----------------")
    opcao = int(input("Opção: "))
    return opcao


def cadastrar():
    if len(banco) == 0:
        nome = input("Digite o nome do aluno: ")
        banco.append(nome)
        for i in range(5):
            nota = float(input(f"Digite a nota {i+1}: "))
            banco.append(nota)
        print(f"{nome} cadastrado com sucesso!")
    else:
        print("[erro] já existe usuário cadastrado")

def mostrar():
    if len(banco) != 0:
        print(f"Notas do {banco[0]}:")
        for i in range(1, len(banco)):
            print(f"- {banco[i]}")
    else:
        print("banco vazio...")

def atualizar():
    print(banco)
    id = int(input("Digite o índice do que você quer atualizar: "))
    banco[id] = input("Digite o novo valor: ")

def deletar():
    # banco = [] # Poderia ter sido mais fácil
    tamanho = len(banco)
    for i in range(tamanho):
        banco.pop()


banco = []
while True:
    opcao = menu()
    if opcao == 0:
        print("Saindo...")
        break
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        mostrar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        deletar()