# Faça um programa para ler um número inteiro N (positivo ou negativo) do usuário e escreva todos os números de N até zero (inclusive)

start = int(input("Número: "))

if start > 0:
    while start >= 0:
        print(start)
        start = start -1
else:
    while start <= 0:
        print(start)
        start = start + 1

print("Fim")