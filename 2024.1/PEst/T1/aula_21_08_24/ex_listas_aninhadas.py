# Crie uma lista de listas com 3 elementos em cada e mostre elemento a elemento dessa lista de listas.

L = [[10, 20, 30], ['a', 'b', 'c'], [0, 0, 0]]


for linha in L:
    for coluna in linha:
        print(coluna)


for i in range(3):
    for j in range(3):
        print(L[i][j])
