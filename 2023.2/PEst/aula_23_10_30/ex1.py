# Crie um programa que peça ao usuário para
# especificar o número de linhas e colunas de uma
# matriz. Em seguida, preencha a matriz com números
# inteiros fornecidos pelo usuário. Use listas
# aninhadas para representar a matriz.

numero_de_linhas = int(input("Linhas: "))
numero_de_colunas = int(input("Colunas: "))

matriz = []

for i in range(numero_de_linhas):
    linha = []
    for j in range(numero_de_colunas):
        elemento = input("Elemento: ")
        linha.append(elemento)
    matriz.append(linha)


for linha in matriz:
    print(linha)
