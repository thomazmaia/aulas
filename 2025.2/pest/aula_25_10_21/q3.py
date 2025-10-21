# Refaça o programa anterior usando funções. A sua função deve receber uma lista e retornar o maior número.

def maior_numero(lista_de_numeros):
    max = lista_de_numeros[0]

    for i in range(len(lista)):
        if lista_de_numeros[i] > max:
            max = lista_de_numeros[i]
    
    return max

lista = [1, 2, 8, 15, -8, 50, 2, 20, 22, 18, 3, 10]

print(maior_numero(lista))