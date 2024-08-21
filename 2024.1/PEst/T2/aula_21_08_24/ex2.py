# 2. Crie um programa que permita ao usuário registrar informações de alunos, incluindo nome, idade e notas em várias disciplinas. Use uma lista aninhada para representar os alunos, onde cada aluno é uma lista com seu nome, idade e uma lista de notas. O programa deve permitir adicionar novos alunos, remover alunos existentes e calcular a média de notas de cada aluno.

def menu():
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Calcular a média")
    print("4 - Sair")
    print("5 - Mostrar alunos")
    op = int(input("Digite a opção: "))
    return op


def adicionar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input(f"Idade de {nome}: "))
    quantidade_de_notas = int(input("Quantas notas: "))
    notas = []
    for i in range(quantidade_de_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    aluno = [nome, idade, notas]
    lista_de_alunos.append(aluno)
    

def remover_aluno():
    nome = input("Digite o nome do aluno: ")
    for aluno in lista_de_alunos:
        if nome == aluno[0]:
            lista_de_alunos.remove(aluno)
            print(f"{nome} removido com sucesso!")
            break
    

def calcular_media():
    for aluno in lista_de_alunos:
        lista_de_notas = aluno[2]
        soma = 0
        for nota in lista_de_notas:
            soma += nota
        media = soma/len(lista_de_notas)
        print(f"Média de {aluno[0]} = {media}")

def mostrar_alunos():
    for aluno in lista_de_alunos:
        print(aluno)


lista_de_alunos = []
while True:
    opcao = menu()
    if opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        remover_aluno()
    elif opcao == 3:
        calcular_media()
    elif opcao == 4:
        break
    elif opcao == 5:
        mostrar_alunos()
    else:
        print("Opção inválida")