# Crie um programa que peça ao usuário para especificar o número de linhas e colunas de uma matriz. Em seguida, preencha a matriz com números inteiros fornecidos pelo usuário. Use listas aninhadas para representar a matriz.

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

matriz = []
for i in range(linhas):
    aux = []
    for j in range(colunas):
        val = int(input(f"Digite o valor de  [{i}][{j}]: "))
        aux.append(val)
    matriz.append(aux)


for linha in matriz:
    print(linha)