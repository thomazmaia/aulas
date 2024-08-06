# 4. Escreva um programa que encontre o maior número em uma lista de números inteiros. Use o loop FOR para percorrer a lista.

L = [10, 20, 4, 85, 32, 0]
aux = 0

for numero in L:
    if numero > aux:
        aux = numero

print(aux)