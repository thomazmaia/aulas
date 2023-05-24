def estoque(lista):
    nova_lista = []
    for tupla in lista:
        if tupla[1] > 10:
            nova_lista.append(tupla)
    return nova_lista


lista_produtos = [("Camiseta", 15), ("Calça", 5), ("Tênis", 20), ("Boné", 8)]

print(estoque(lista_produtos))  # deve imprimir [("Camiseta", 15), ("Tênis", 20)]
