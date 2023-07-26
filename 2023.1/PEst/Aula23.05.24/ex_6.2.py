def intersecao(l1, l2):
    res = []
    for item in l1:
        if item not in res:
            res.append(item)
    for item in l2:
        if item not in res:
            res.append(item)
    return tuple(res)


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 4, 5, 6, 7]

novo_conjunto = intersecao(lista1, lista2)
print(novo_conjunto)
