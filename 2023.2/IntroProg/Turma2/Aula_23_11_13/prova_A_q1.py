# Suponha que o preço de capa de um livro seja R$ 24,95 mas as 
# livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 
# para o primeiro exemplar e 75 centavos para cada exemplar adicional.
# Escreva um programa para calcular o custo total de N cópias.

N = int(input("Quantidade de livros: "))
preco_livro = 24.95
desconto = 40/100

valor_desconto = desconto*preco_livro
preco_livro_com_desconto = preco_livro - valor_desconto

frete = 3 + 0.75 * (N-1)

valor_final = preco_livro_com_desconto*N + frete
print(valor_final)