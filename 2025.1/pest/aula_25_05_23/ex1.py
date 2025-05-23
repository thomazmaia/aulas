# 1. Crie uma lista de listas com 3 elementos em cada e mostre elemento a elemento dessa lista de listas.

lista = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print("Forma 1:")
for linha in lista:
    for coluna in linha:
        print(coluna)

print("Forma 2:")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j])