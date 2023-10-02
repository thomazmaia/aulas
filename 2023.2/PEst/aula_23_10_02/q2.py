# Escreva um programa que encontre o maior número em uma lista de números
# inteiros. Use um loop for para percorrer a lista.

L = [10, 8, 7, 29, 4, 100, 99, -4, 6, 3, 20]

maior = -999999999

for numero in L:
    if numero > maior:
        maior = numero


print(f"Maior número da lista: {maior}")
