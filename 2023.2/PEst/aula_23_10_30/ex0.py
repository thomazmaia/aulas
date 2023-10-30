# Crie uma lista de listas com 3 elementos em cada
# e mostre elemento a elemento dessa lista de listas

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in L:
    print("Linha:")
    for coluna in linha:
        print(coluna)
