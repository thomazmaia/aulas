# Faça um programa para ler um número e dizer se ele
# é positivo, negativo ou zero

num = float(input("Número: "))

if num > 0:
    print(f"O número {num} é positivo")
else:
    if num < 0:
        print(f"O número {num} é negativo")
    else:
        print(f"O número {num} é zero")
