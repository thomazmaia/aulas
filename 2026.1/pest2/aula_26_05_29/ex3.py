# ## Exercício 3 - Maior número

# Crie um programa que:

# - Leia 5 números inteiros
# - Armazene os números em uma lista
# - Mostre o maior número da lista

def acha_maior(lista : list):
    # 4, 10, 3, 7, 2
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    
    return maior
    

L = [0, 0, 0, 0, 0]

for i in range(5):
    L[i] = int(input("Digite um número: "))

print(L)

print(f"Maior número: {acha_maior(L)}")