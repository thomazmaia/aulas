# Desenvolva um programa que leia 5 números e guarde-os em uma tupla. Ao final mostre:
# - Quantas vezes o número 1 apareceu.
# - Em que posição foi digitado o primeiro 0.
# - Quais foram os números ímpares

tupla = ()

for i in range(5):
    N = int(input(f"Número {i}: "))
    tupla += tuple([N])

contador = 0
impares = 0
posicao = -1

for i in range(len(tupla)):
    item = tupla[i]
    if item == 1:
        contador += 1
    if item == 0:
        posicao = i        
    if item % 2 == 1:
        impares += 1

print(tupla)
print(f"1s: {contador}")
print(f"Posição do zero: {posicao}")
print(f"Impares: {impares}")