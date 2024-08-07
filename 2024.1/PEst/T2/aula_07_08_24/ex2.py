# Crie um programa que tenha a função "add_lista_unico(lista, elemento)". Essa função deve receber uma lista e um elemento. Você deve adicionar o elemento recebido à lista recebida e, ao final, a função deve retornar a lista modificada.
# OBS: o elemento só deve ser adicionado se ele já não existir na lista. Ou seja, a lista não aceita elementos repetidos.

def add_lista_unico(lista:list, elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista

L = []
print(add_lista_unico(L, 87))
print(add_lista_unico(L, 87))
print(add_lista_unico(L, "oi"))
print(add_lista_unico(L, 87))