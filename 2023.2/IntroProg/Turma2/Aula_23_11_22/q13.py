# 13. Faça um programa utilizando o laço while para ler 10 números e informar o maior e o menor número lido.

contador = 1
maior_atual = -99999999
menor_atual = 99999999

while contador <= 10:
    N = int(input("Digite um número: "))
    if N > maior_atual:
        maior_atual = N
    if N < menor_atual:
        menor_atual = N
    contador += 1

print(f"Maior: {maior_atual}")
print(f"Menor: {menor_atual}")