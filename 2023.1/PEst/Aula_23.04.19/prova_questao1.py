# Questão 1
def manipula_lista(lista):
    lista.append(4)
    lista = [1, 2, 3]
    return lista

minha_lista = [5, 6, 7]
nova_lista = manipula_lista(minha_lista)
print(minha_lista)   # [5, 6, 7, 4]
print(nova_lista)    # [1, 2, 3]