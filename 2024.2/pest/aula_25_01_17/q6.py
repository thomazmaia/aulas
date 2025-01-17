# 6. Escreva um programa que encontre o maior número em uma lista de números inteiros. Use um loop for para percorrer a lista.

lista = [20, 76, 94, 60, 28, 65, 4, 69, 71, 22]

maior = lista[0]

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]

print(f"O maior número da lista é o {maior}")

