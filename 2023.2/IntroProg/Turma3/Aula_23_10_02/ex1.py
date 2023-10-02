# Faça um programa para ler um número e dizer se ele
# é positivo, negativo ou zero.

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"{numero} é positivo")
elif numero < 0:
    print(f"{numero} é negativo")
else:
    print(f"{numero} é zero")
