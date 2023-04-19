def gera_lista(tamanho=0):
    lista = []
    for i in range(tamanho):
        lista.append(i)
    return lista

lista1 = gera_lista()
print(lista1)

lista2 = gera_lista(tamanho=3)
print(lista2)