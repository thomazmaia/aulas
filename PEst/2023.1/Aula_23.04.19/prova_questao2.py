def multiplica_lista(lista, fator):
    for i in range (len(lista)):
        lista[i] = lista[i] * fator

minha_lista = [1, 2, 3]
nova_lista = multiplica_lista(minha_lista, 2)
print(minha_lista)
print(nova_lista)