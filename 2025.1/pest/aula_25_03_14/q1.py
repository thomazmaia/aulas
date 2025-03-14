numero = int(input("Digite um número: "))

pares = "não é par"
impares = "não é ímpar"

if (numero == 0):
    print("Zero é neutro")
elif (numero % 2 == 0):
    pares = numero
else:
    impares = numero


print(pares)
print(impares)