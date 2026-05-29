# Crie um programa que tenha uma função chamada conta_pares. Essa função deve receber uma lista de números inteiros e retornar a quantidade de números pares nessa lista.

def eh_par(N : int):
    if N % 2 == 0:
        return True
    return False

def conta_pares(lista : list):
    contador = 0
    for item in lista:
        if eh_par(item):
            contador += 1
    
    return contador

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 190, 100, 8]

print(conta_pares(L))