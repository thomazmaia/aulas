# Suponha que o preço de capa de um livro seja R$ 24,95 mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Escreva um programa para calcular o custo total de N cópias.

N = int(input("Quantidade de livros: "))

preco_capa = 24.95
desconto = 40/100

valor_desconto = desconto * preco_capa
valor_livro = preco_capa - valor_desconto

valor_transporte = 3 + 0.75*(N-1)

preco_total = valor_livro*N + valor_transporte

print(preco_total)