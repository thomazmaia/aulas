# Crie um programa para gerar 5 números aleatórios, coloque-os dentro de uma tupla e encontre o maior e o menor valor da sequência.

import random

tupla = ()

maior = -99999
menor = 999999

for i in range(5):
    tupla += tuple([random.randint(0, 9)])
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]


print(tupla)
print(f"Maior = {maior}")
print(f"Menor = {menor}")