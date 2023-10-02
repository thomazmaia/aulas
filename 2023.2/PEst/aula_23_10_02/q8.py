# Refaça o programa anterior usando funções. A sua função deve receber uma
# lista e retornar outra lista com duas posições, sendo a primeira posição o
# menor número e a segunda o maior.


def pega_maior_e_menor(lista):
    outra_lista = [0, 0]

    maior = -999999
    menor = 9999999

    for indice in range(len(lista)):
        if lista[indice] > maior:
            maior = lista[indice]
        if lista[indice] < menor:
            menor = lista[indice]

    outra_lista[0] = menor
    outra_lista[1] = maior
    return outra_lista


lista_original = [3, 10, 9, -10, -4, 76, -21, 0, 56, 87, 34, 60]

minha_lista = pega_maior_e_menor(lista_original)
print(f"Maior: {minha_lista[1]}")
print(f"Menor: {minha_lista[2]}")
