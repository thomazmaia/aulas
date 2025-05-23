# 2. Crie um programa que peça ao usuário para especificar o número de linhas e colunas de uma matriz. Em seguida, preencha a matriz com números inteiros fornecidos pelo usuário. Use listas aninhadas para representar a matriz.

num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))

matriz = []

for i in range(num_linhas):
    linha = []    
    for j in range(num_colunas):
        elemento = int(input(f"Digite o elemento ({i+1},{j+1}): "))
        linha.append(elemento)
    matriz.append(linha)

print("Printando a matriz...")
for linha in matriz:
    print(linha)