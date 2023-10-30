# 1. Peça ao usuário para digitar um número e, em seguida, verifique se o número
# é positivo, negativo ou igual a zero. Imprima a resposta correspondente.

numero = float(input("Número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número é zero")
