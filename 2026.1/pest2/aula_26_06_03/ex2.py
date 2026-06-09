def eh_par(N):
    if N % 2 == 0:
        return True
    return False

def pega_pares(lista : list):
    nova_lista = []
    for item in lista:
        if eh_par(item):
            nova_lista.append(item)

    return nova_lista


L = [1, 2, 3, 10, 17, 88, 99]
print(L)
print(pega_pares(L))