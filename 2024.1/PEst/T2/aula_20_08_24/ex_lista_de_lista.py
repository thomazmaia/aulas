# Crie uma lista de listas com 3 elementos em cada e mostre elemento a elemento dessa lista de listas.


elemento1 = [1, 2, 3]
elemento2 = [4, 5, 6]
elemento3 = [7, 8, 9]

#L = [elemento1, elemento2, elemento3]
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in L:
    for coluna in linha:
        print(coluna)