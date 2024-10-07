# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias

preco_livro = 24.95
desconto = 40/100

valor_desconto = preco_livro * desconto
preco_livro_com_desconto = preco_livro - valor_desconto

print(f"Desconto = R${valor_desconto}")
print(f"Livro com desconto = R${preco_livro_com_desconto}")

numero_copias = 60

preco_60_copias = numero_copias * preco_livro_com_desconto

print(f"Preço para as {numero_copias} cópias = R${preco_60_copias}")

preco_transporte = 3.00 + 0.75*(numero_copias - 1)

custo_total = preco_60_copias + preco_transporte

print(f"Custo total das {numero_copias} cópias = R${custo_total}")