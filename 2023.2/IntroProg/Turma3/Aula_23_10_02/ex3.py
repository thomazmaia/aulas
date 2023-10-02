# Faça um programa de uma empresa de telefonia. Os planos
# da empresa oferecem diferentes preços de acordo com a
# quantidade de minutos usados por mês:
# Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto
# Entre 200 e 400 minutos, a empresa cobra R$ 0,18 por minuto
# Acima de 400 minutos, o preço do minuto é de R$ 0,15.
#
# Leia a quantidade de minutos e diga o preço a pagar.

min = int(input("Minutos: "))

if min < 200:
    preco_final = min * 0.20
elif min >= 200 and min <= 400:
    preco_final = min * 0.18
else:
    preco_final = min * 0.15

print(f"{min} minutos custam R$ {preco_final}")
