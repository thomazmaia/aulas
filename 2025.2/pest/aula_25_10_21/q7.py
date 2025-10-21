# Escreva um programa que encontre o maior e o menor número em uma lista de números inteiros. Use um loop for para percorrer a lista.

lista = [1, 2, 8, 15, -8, 50, -20, 20, 22, 18, 3, 100]

max = lista[0]

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]

print(f"O maior número é {max}")

min = lista[0]

for i in range(len(lista)):
    if lista[i] < min:
        min = lista[i]

print(f"O menor número é {min}")