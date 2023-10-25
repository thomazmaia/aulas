# Escreva uma função chamada adicionar_elemento que aceite três parâmetros:
# uma lista lst, um índice indice e um elemento elemento. A função deve inserir
# o elemento na lista lst no índice especificado. Lembre-se de que o índice pode
# ser maior que o tamanho atual da lista.


def adicionar_elemento(lst, indice, elemento):
    lst.insert(indice, elemento)


L = [1, 2, 3, 4]
print(f"Lista antes: {L}")
adicionar_elemento(L, 2, "oi")
print(f"Lista depois: {L}")
