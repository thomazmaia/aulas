# Dada uma lista de números inteiros, crie um programa que remova todos os números pares da lista usando o método 'remove'. Em seguida, imprima a lista resultante.

numeros = [1, 3, 10, 3, 6, 34, 52, 23, 62, 10, 3, 65, 74]
# numeros_copia = numeros.copy()
numeros_copia = numeros[:] # Cópia de lista

for elemento in numeros_copia:
    if elemento % 2 == 0:
        numeros.remove(elemento)

print(numeros)