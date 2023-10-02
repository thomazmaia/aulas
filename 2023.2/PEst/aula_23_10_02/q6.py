# Escreva um programa que percorra uma lista de números e crie
# uma nova lista que contenha apenas os números pares da lista
# original.

L = [2, 3, 10, 99, 76, 45, 37, 82, 94, 32, 58, 21]
lista_pares = []
lista_impares = []

for item in L:
    if item % 2 == 0:
        print(f"{item} é par")
        lista_pares.append(item)
    else:
        print(f"{item} é ímpar")
        lista_impares.append(item)

print(f"Lista dos pares: {lista_pares}")
print(f"Lista dos ímpares: {lista_impares}")
