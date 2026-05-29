# ## Exercício 2 - Quantidade de aprovados

# Crie um programa que:

# - Leia as notas de 6 alunos
# - Armazene as notas em uma lista
# - Conte quantos alunos tiveram nota maior ou igual a 7

def conta_nota(lista : list, corte : int = 7):
    contador = 0
    for item in lista:
        if item >= corte:
            contador += 1

    return contador


notas = [0, 0, 0, 0, 0, 0]

for i in range(6):
    notas[i] = float(input(f"Digite a nota {i+1}: "))

print(notas)

print(conta_nota(notas, 7))