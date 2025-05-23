# 3. Crie um programa que permita ao usuário registrar informações de alunos, incluindo nome, idade e notas em várias disciplinas. Use uma lista aninhada para representar os alunos, onde cada aluno é uma lista com seu nome, idade e uma lista de notas. O programa deve permitir adicionar novos alunos, remover alunos existentes e calcular a média de notas de cada aluno.

# Exemplo: 
# xico = ['Francisco', 18, [8.8, 9, 7]]
# maria = ['Maria', 17, [10, 10, 8]]
# alunos = [xico, maria]
# alunos = [['Francisco', 18, [8.8, 9, 7]], 
#           ['Maria', 17, [10, 10, 8]]]

alunos = []

def menu_geral():
    print("[0] - Sair")
    print("[1] - Adicionar aluno")
    print("[2] - Calcular média")
    print("[3] - Mostar alunos")
    opcao = int(input("Digite a opção: "))
    return opcao

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input(f"Digite a idade do(a) {nome}: "))
    qtd_notas = int(input(f"Quantas provas {nome} fez? "))
    notas = []
    for i in range(qtd_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    alunos.append([nome, idade, notas])

while True:
    op = menu_geral()
    if op == 0:
        break  
    elif op == 1:
        adicionar_aluno()
    elif op == 2:
        pass #calcular_media()
    elif op == 3:
        for aluno in alunos:
            print(aluno)