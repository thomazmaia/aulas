# Crie um programa que permita ao usuário registrar
# informações de alunos incluindo nome, matrícula e
# notas em várias disciplinas. Use uma listra aninhada
# para representar os alunos, onde cada aluno é uma
# lista com três elementos: nome, matrícula e uma
# lista de notas. O programa deve permitir adicionar
# novos alunos.


def pegar_dados():
    aluno = []
    nome = input("Nome: ")
    matricula = int(input("Matrícula: "))
    qtd_de_notas = int(input("Quantas notas? "))
    notas = pegar_notas(qtd_de_notas)
    aluno.append(nome)
    aluno.append(matricula)
    aluno.append(notas)
    return aluno


def pegar_notas(qtd):
    notas = []
    for i in range(qtd):
        notas.append(float(input(f"Nota {i}: ")))
    return notas


def mostra_alunos(alunos):
    for item in alunos:
        print(item)


add_aluno = True
alunos = []
while add_aluno:
    aluno = pegar_dados()
    alunos.append(aluno)

    temp = input("Digite S para sair: ")
    if temp in "sS":
        add_aluno = False

mostra_alunos(alunos)
