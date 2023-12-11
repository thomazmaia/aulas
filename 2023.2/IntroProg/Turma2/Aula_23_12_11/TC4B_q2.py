quantidade_de_produtos = int(input("Quantidade de produtos: "))

contador = 1
soma = 0

while contador <= quantidade_de_produtos:
    preco = float(input(f"Produto {contador}: "))
    soma = soma + preco
    contador += 1

print(f"Somatório de preços: R$ {soma}")
preco_medio = soma/quantidade_de_produtos
print(f"Preço médio de cada produto: R$ {preco_medio}")