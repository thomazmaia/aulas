# 8. Escreva uma função que receba duas listas e retorne a lista com mais elementos

def verifica_quem_tem_mais(lista1, lista2):
    if len(lista1) >= len(lista2):
        return lista1
    else:
        return lista2

print( verifica_quem_tem_mais([0, 1, 'dois'], ['zero']) )

print( verifica_quem_tem_mais([True, False, 'true'], [1, 2, 3, 4, 5]) )