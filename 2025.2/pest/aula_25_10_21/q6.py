# Escreva um programa que percorra uma lista de números e crie uma nova lista que contenha apenas os números pares da lista original.

lista = [1, 2, 8, 15, 17, 4]

nova_lista = ['', '', '', '', '', '']

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        nova_lista[i] = lista[i]

print(nova_lista)