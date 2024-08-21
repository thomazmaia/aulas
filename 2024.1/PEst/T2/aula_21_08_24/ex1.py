# 1. Crie um programa que peça ao usuário para especificar o número de linhas e colunas de uma matriz. Em seguida, preencha a matriz com números inteiros fornecidos pelo usuário. Use listas aninhadas para representar a matriz.

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor da posição: [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)