# Crie um programa que peça ao usuário para especificar o número de linhas e colunas de uma matriz. Em seguida, preencha a matriz com números inteiros fornecidos pelo usuário. Ao final, mostre a matriz resultante.
# OBS: Use listas aninhadas!

# Criar e preencher a matriz
linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input("Digite um número: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)