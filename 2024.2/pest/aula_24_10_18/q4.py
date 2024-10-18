# 4. Escreva um programa em Python para somar três números inteiros do usuário. No entanto, se dois valores forem iguais, a soma será zero.

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

if (numero1 != numero2) and (numero2 != numero3):
    soma = numero1 + numero2 + numero3
else:
    soma = 0

print(soma)