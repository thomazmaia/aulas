# ## Exercício 2 - Quantidade de aprovados

# Crie um programa que:

# - Leia as notas de 6 alunos
# - Armazene as notas em uma lista
# - Conte quantos alunos tiveram nota maior ou igual a 7

def conta_alunos(lista : list, nota : int):
    contador = 0
    for elemento in lista:
        if elemento >= nota:
            contador += 1

    return contador


notas = [0, 0, 0, 0, 0, 0]

for i in range (6):
    notas[i] = float(input(f"Digite a nota do aluno {i+1}: "))


quantidade_de_alunos = conta_alunos(notas, 7)
print(f"{quantidade_de_alunos} notas >= 7")