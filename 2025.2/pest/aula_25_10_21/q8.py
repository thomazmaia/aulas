# Refaça o programa anterior usando funções. A sua função deve receber uma lista e retornar outra lista com duas posições, sendo a primeira posição o menor número e a segunda o maior.

def maior_menor(lista):
    max = lista[0]

    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]

    min = lista[0]

    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]

    nova_lista = [min, max]
    return nova_lista





lista = [1, 2, 8, 15, -8, 50, -2, 20, 22, 18, 30]

resultado = maior_menor(lista)

print(f"Menor: {resultado[0]}")
print(f"Maior: {resultado[1]}")