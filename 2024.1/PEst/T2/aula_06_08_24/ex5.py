# 5. Refaça o programa anterior usando funções. Sua função deve receber uma lista e retornar o maior número da lista.

def maior_numero(lista:list):
    aux = 0
    for numero in L:
        if numero > aux:
            aux = numero    
    return aux


L = [10, 20, 4, 15, 32, 0]

print(maior_numero(L))