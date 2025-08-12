qtd_livros = int(input("Digite a quantidade de livros: "))
val_livro = 24.95
desconto = 40/100

val_desconto = desconto * val_livro
print(f"Valor do desconto: R$ {val_desconto}")

val_livro_final = val_livro - val_desconto
print(f"Valor do livro com desconto: R$ {val_livro_final}")

val_frete = 3.00 + 0.75 * (qtd_livros - 1)

val_final = qtd_livros * val_livro_final + val_frete
print(f"Valor total da compra: R$ {val_final}")