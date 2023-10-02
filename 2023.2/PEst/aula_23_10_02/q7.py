# Escreva um programa que encontre o maior e o menor número em uma
# lista de números inteiros. Use um loop for para percorrer a
# lista.

L = [3, 10, 9, -10, -4, 76, -21, 0, 56, 87, 34, 60]

maior = -9999999
menor = 99999999

for item in L:
    if item > maior:
        maior = item
    if item < menor:
        menor = item

print(f"Maior: {maior}")
print(f"Menor: {menor}")
