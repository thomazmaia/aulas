# 3. Refaça o programa anterior usando funções. Sua função deve receber uma lista e retornar o maior número da lista.

def retorna_maior(L : list):
    maior_numero = L[0]

    for item in L:
        if item > maior_numero:
            maior_numero = item   

    return maior_numero



lista_de_numeros = [10, -12, 200, 13]

print(retorna_maior(lista_de_numeros))