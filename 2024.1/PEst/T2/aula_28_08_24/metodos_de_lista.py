# append() - Adiciona um elemento ao final da lista
lista = ['um', 'dois', 'três']
lista.append(4)
print("append()", lista)

# insert() - Adiciona um elemento em uma posição específica
lista = ['um', 'dois', 'três']
lista.insert(1, 4)
print("insert()", lista)

# remove() - Remove o item com o valor especificado
lista = ['um', 'dois', 'três']
lista.remove("dois")
print("remove()", lista)

# pop() - Remove o elemento em uma posição específica
lista = ['um', 'dois', 'três']
lista.pop(1) # se não tiver argumento, remove o último
print("pop()", lista)

# sort() - Ordena a lista
lista = [1, 4, 10, 7, 6, 6, 3, 2]
lista.sort(reverse=False) # False = crescente; True = decrescente
print("sort()", lista)

# clear() - Remove todos os elementos da lista
lista = [1, 4, 10, 7, 6, 6, 3, 2]
lista.clear()
print("clear()", lista)

# copy() - Faz uma cópia da lista
lista = [1, 4, 10, 7, 6, 6, 3, 2]
lista2 = lista.copy() # lista[:]
print("copy()", lista2)

# count() - Retorna o número  de vezes que aquele elemento aparece
lista = [1, 4, 10, 7, 6, 6, 6, 3, 2]
x = lista.count(6)
print("count()", x)

# index() - Retorna o índice da primeira ocorrência do elemento
lista = [1, 2, 6, 3, 4, 6, 5, 6]
x = lista.index(6) # Erro se o elemento não existir
print("index()", x)

# extend() - Adiciona elementos de uma lista ao final de outra lista
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista1.extend(lista2)
print("extend()", lista1)
print("extend()", lista2)