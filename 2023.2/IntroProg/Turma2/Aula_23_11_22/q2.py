# 2. Faça um programa para ler um número N do usuário e escreva todos os números de N até zero (inclusive).

numero = int(input("Número: "))

while numero >= 0:
    print(numero)
    numero -= 1     # numero = numero - 1

