# Crie um programa que permita ao usuário registrar
# informações de alunos incluindo nome, matrícula e
# notas em várias disciplinas. Use uma listra aninhada
# para representar os alunos, onde cada aluno é uma
# lista com três elementos: nome, matrícula e uma
# lista de notas. O programa deve permitir adicionar
# novos alunos e removê-los pelo número de matrícula.


def add_aluno():
    aluno = []
    nome = input("Nome: ")
    matricula = int(input("Matrícula: "))
    qtd_de_notas = int(input("Quantas notas? "))
    notas = pegar_notas(qtd_de_notas)
    aluno.append(nome)
    aluno.append(matricula)
    aluno.append(notas)
    alunos.append(aluno)


def rem_aluno():
    matricula = int(input("Digite a matricula que deseja remover: "))
    for aluno in alunos:
        if aluno[1] == matricula:
            nome = aluno[0]
            alunos.remove(aluno)
            print(f"{nome} removido com sucesso.")

def atualiza_aluno():
    mostra_alunos()    
    print("Pelo que você gostaria de atualizar?")
    print("N - Pelo Nome")
    print("M - Pela Matrícula")
    op = input("Opcao: ")
    if op in "nN":
        nome = input("Nome: ")
        for item in alunos:
            if item[0] == nome:
                novo_nome = input("Novo nome: ")
                item[0] = novo_nome
    elif op in "mM":
        matricula = int(input("Matricula: "))
        for item in alunos:
            if item[1] == matricula:
                nova_matricula = input("Nova matricula: ")
                item[1] = nova_matricula

def pegar_notas(qtd):
    notas = []
    for i in range(qtd):
        notas.append(float(input(f"Nota {i}: ")))
    return notas


def mostra_alunos():
    for item in alunos:
        print(item)


def menu():
    print("0 - Adicionar")
    print("1 - Remover")
    print("2 - Mostrar")
    print("3 - Atualizar")
    print("4 - Sair")
    opcao = int(input("Opção: "))
    return opcao

alunos = []
while True:
    opcao = menu()
    if opcao == 0:
        add_aluno()
    elif opcao == 1:
        rem_aluno()
    elif opcao == 2:
        mostra_alunos()
    elif opcao == 3:
        atualiza_aluno()
    elif opcao == 4:
        break
