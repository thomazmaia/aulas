# Faça um programa para ler um número inteiro N (positivo ou negativo) do usuário e escreva todos os números de zero até N (inclusive)

start = 0
end = int(input("Número: "))

if end > 0:
    while end >= start:
        print(start)
        start = start + 1
else:
    while end <= start:
        print(start)
        start = start - 1

print("Fim")