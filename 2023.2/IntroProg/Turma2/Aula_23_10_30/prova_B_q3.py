qtd_hamburguer = int(input("Hamburgueres: "))
qtd_batata = int(input("Batatas: "))
qtd_refri = int(input("Refrigerantes: "))

valor_hamburguer = qtd_hamburguer * 10
valor_batata = qtd_batata * 5
valor_refri = qtd_refri * 3

valor_total = valor_hamburguer + valor_batata + valor_refri

if valor_total > 50:
    desconto = (10 / 100) * valor_total
    valor_final = valor_total - desconto
    print(f"Valor final: R$ {valor_final} com desconto de R$ {desconto}")
else:
    print(f"Valor final: R$ {valor_total} sem desconto")
