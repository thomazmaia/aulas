# 2. Escreva um programa que encontre o maior número em uma lista de números inteiros. Use o loop FOR para percorrer a lista.

lista_de_numeros = [-1, -3, -4.5, -9, -5.7, -12.3, -20.4, -12.3]

maior_numero = lista_de_numeros[0]

for item in lista_de_numeros:
    if item > maior_numero:
        maior_numero = item

print(maior_numero)