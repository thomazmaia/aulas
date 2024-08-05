# Removendo elementos da lista - REMOVE
L = [3, 4, 10, 4, 3, 8, 5, 0]

print(L)
L.remove(10)
print(L)

# Faça uma função para receber uma lista e um elemento. Caso esse elemento exista dentro da lista, remova-o. Caso não exista, adicione ao final da lista.
# Sua função não deve retornar nada.

def add_remover(L : list, elemento):
    if elemento in L:
        L.remove(elemento)
    else:
        L.append(elemento)


lista = list()
for i in range(3):
    add_remover(lista, input("Digite alguma coisa: "))
    print(lista)