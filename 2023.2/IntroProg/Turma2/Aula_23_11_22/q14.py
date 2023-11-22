# 14. Faça um programa utilizando o laço while para ler 5 números e informar a soma e a média desses números.

contador = 1
soma = 0
qtd_de_numeros = 2

while contador <= qtd_de_numeros:
    N = int(input("Número: "))
    soma = soma + N
    contador += 1


print(f"Soma = {soma}")
print(f"Média = {soma/qtd_de_numeros}")