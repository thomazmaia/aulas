# ## Exercício 6 - Estoque baixo

# Crie um programa que:

# - Leia a quantidade em estoque de 5 produtos
# - Armazene as quantidades em uma lista
# - Mostre quantos produtos estão com estoque menor que 10

def conta_produto(lista : list, corte : int = 10):
    contador = 0
    for item in lista:
        if item < corte:
            contador += 1

    return contador

produtos = [0, 0, 0, 0, 0]

for i in range(5):
    produtos[i] = int(input("Digite a quantidade: "))

print(produtos)
print(conta_produto(produtos))