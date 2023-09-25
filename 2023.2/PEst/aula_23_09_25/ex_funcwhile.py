def mostra_pares(lista):
    tamanho = len(lista)
    indice = 0

    while indice < tamanho:
        elemento = lista[indice]
        if elemento % 2 == 0:
            print(f"{elemento} é par")
        indice += 1


L1 = [8, 10, 45, 78, 13, 64, 0, 1, 2]
mostra_pares(L1)
