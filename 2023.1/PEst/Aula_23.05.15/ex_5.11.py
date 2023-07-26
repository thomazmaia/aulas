produtos = {}

produto = input("Digite o produto: ")
categoria = input(f"Qual a categoria do {produto}: ")
preco = float(input(f"Digite o preço do {produto}: "))

produtos[produto] = {"categoria": categoria, "preco": preco}

print(produtos)
