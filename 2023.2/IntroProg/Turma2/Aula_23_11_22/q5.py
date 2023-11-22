# 5. Faça um programa para ler dois números M e N positivos não iguais e mostre todos os números entre M e N de maneira crescente (do menor para o maior).

M = int(input("Número: "))
N = int(input("Número: "))

if M > N:
    menor = N
    maior = M
else:
    menor = M
    maior = N

while menor <= maior:
    print(menor)
    menor += 1