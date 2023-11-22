# 11. Faça um programa para ler um número N positivo e mostrar todos os números inteiros de N até 0 e, ao final, mostre a soma desses números.

N = int(input("Número: "))

contador = N
acumulador = 0

while contador >= 0:
    print(contador)
    acumulador += contador
    contador -= 1

print(f"Soma = {acumulador}")