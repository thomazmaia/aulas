# Escreva um programa que encontre o maior número em uma lista de números inteiros. Use um loop for para percorrer a lista.

lista = [1, 2, 8, 15, -8, 50, 2, 20, 22, 18, 3, 100]

max = lista[0]

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]

print(f"O maior número é {max}")