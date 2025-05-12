# 2. Escreva um programa que encontre o maior número em uma lista de números inteiros. Use um loop for para percorrer a lista.
# 3. Refaça o programa anterior usando funções. A sua função deve receber uma lista e retornar o maior número.


def pega_maior_valor(lista : list):
    temp = lista[0]
    for numero in lista:
        if numero > temp:
            temp = numero
    return temp


lista = [1, 10, -3, 40, 35, 780, -110, 1000]
val = pega_maior_valor(lista)
print(f"O maior valor é {val}")