# Crie um programa que tenha uma função chamada pega_pares. Essa função deve receber uma lista de números inteiros e retornar uma nova lista somente com os números pares da lista anterior.

def eh_par(N : int):
    if N % 2 == 0:
        return True
    return False

def pega_pares(lista : list):
    resultado = []
    for item in lista:
        if eh_par(item):
            resultado.append(item)
    
    return resultado

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 190, 100, 8]

print(pega_pares(L))