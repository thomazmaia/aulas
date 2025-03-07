preco_livro = 24.95
desconto = 40/100
num_copias = 60

valor_desc = desconto * preco_livro

preco_livro_com_desc = preco_livro - valor_desc

print(f"Valor do desconto: R$ {valor_desc}")
print(f"Preço do livro: R$ {preco_livro_com_desc}")

valor_total_livros = num_copias * preco_livro_com_desc

print(f"Valor total dos livros: R$ {valor_total_livros}")

frete = 3 + (num_copias - 1)*0.75

print(f"Valor do frete: R$ {frete}")

valor_total_compra = valor_total_livros + frete
print(f"--------\nValor total da compra: R$ {valor_total_compra}")