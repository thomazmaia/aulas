# Escreva uma função chamada remover_elemento que aceite uma lista lst e um
# elemento elemento. A função deve remover a primeira ocorrência de elemento da
# lista, se existir. Se o elemento não estiver na lista, a função não deve fazer
# nada.


def remover_elemento(lst, elemento):
    if elemento in lst:
        lst.remove(elemento)


L = [1, 2, 3, 4, 3]
print(f"Lista antes: {L}")
remover_elemento(L, 20)
print(f"Lista depois: {L}")
