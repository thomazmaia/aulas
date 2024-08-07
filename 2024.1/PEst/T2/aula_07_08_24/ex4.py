# Crie um programa que tenha a função "add_del(lista, elemento)". Essa função deve receber uma lista e um elemento. Você deve adicionar o elemento recebido caso ele não esteja na lista. Caso ele esteja você deve removê-lo.
def add_del(lista:list, elemento):
    if elemento in lista:
        lista.remove(elemento)
    else:
        lista.append(elemento)
    return lista

L = []
print(add_del(L, 1))
print(add_del(L, 2))
print(add_del(L, 2))
print(add_del(L, 1))