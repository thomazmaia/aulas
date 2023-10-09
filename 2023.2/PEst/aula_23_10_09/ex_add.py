# Crie um programa que tenha uma função add_lista(lista, elemento).
# Essa função deve receber uma lista e um elemento. Você deve
# adicionar o elemento recebido à lista recebida e, ao final, a
# função deve retornar a lista modificada.


def add_lista(lista, elemento):
    lista.append(elemento)
    return lista


L = []
print(add_lista(L, 10))
print(add_lista(L, 20))
print(add_lista(L, "oi"))
print(add_lista(L, True))
print(add_lista(L, 2.17))
