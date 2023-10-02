# Refaça o programa anterior usando funções. A sua função deve
# receber uma lista e retornar o maior número.


def pega_maior(lista):
    maior = -9999999
    for indice in range(len(lista)):
        if lista[indice] > maior:
            maior = lista[indice]
    return maior


L = [10, 40, -30, 40, 50, 99, 35]

print(f"Maior número: {pega_maior(L)}")
