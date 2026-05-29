# ## Exercício 4 - Maior número e posição

# Crie um programa que:

# - Leia 5 números inteiros
# - Armazene os números em uma lista
# - Mostre:
#     - o maior número
#     - o índice onde ele está

L = [0, 0, 0, 0, 0]

for i in range(5):
    L[i] = int(input("Digite um número: "))

print(L)

maior = L[0]
indice = 0
for i in range(5):
    if L[i] > maior:
         indice = i         
         maior = L[i]

print(f"Maior valor: {maior} no índice {indice}")