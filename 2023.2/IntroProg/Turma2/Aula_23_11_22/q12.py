# 12. Faça um programa utilizando o laço while para ler 5 números e informar o maior número lido.

contador = 1
maior_atual = 0

while contador <= 5:
    N = int(input("Digite um número: "))
    if N > maior_atual:
        maior_atual = N
    contador += 1

print(f"Maior: {maior_atual}")