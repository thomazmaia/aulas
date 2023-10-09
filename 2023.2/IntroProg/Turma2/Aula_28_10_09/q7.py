# Crie um programa que ajude um caixa de supermercado a calcular o preço total das
# compras de um cliente. Solicite ao usuário que insira o preço de três produtos
# diferentes e, em seguida, calcule o preço total. Se o valor total for superior
# a R$ 100, aplique um desconto de 10%. Caso contrário, não aplique desconto.

preco1 = float(input("Preço produto 1: "))
preco2 = float(input("Preço produto 2: "))
preco3 = float(input("Preço produto 3: "))

preco_total = preco1 + preco2 + preco3

if preco_total > 100:
    desconto = (10 / 100) * preco_total
else:
    desconto = 0

print(f"Preço sem desconto: R${preco_total}")
preco_final = preco_total - desconto
print(f"Desconto: R${desconto}")
print(f"Preço final: R${preco_final}")
