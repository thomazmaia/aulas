# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias.

quantidade = int(input("Quantos livros: "))
    
preco_livro = 24.95

desconto = 40/100 # 0.4

preco_livro_com_desconto = 0.6 * preco_livro

valor_frete = 3 + 0.75 * (quantidade - 1)

valor_livros = quantidade * preco_livro_com_desconto

valor_total = valor_frete + valor_livros

print(f"O preço total é de: R$ {valor_total} sendo R$ {valor_livros} de livros e R$ {valor_frete} de tansporte.")