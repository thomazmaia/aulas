# append() - Adiciona um elemento ao final da lista
lista = ['um', 'dois', 'tres']
lista.append(4)
print("append()", lista)

# insert() - Adiciona um elemento em uma posição específica da lista
lista = ['um', 'dois', 'tres']
lista.insert(1, 4)
print("insert()", lista)

# remove() - Remove o elemento com o valor especificado
lista = ['um', 'dois', 'tres']
lista.remove('dois')
print("remove()", lista)

# pop() - Remove o elemento no índice especificado
lista = ['um', 'dois', 'tres']
lista.pop(0) # Retorna o elemento removido
print("pop()   ", lista)

# sort() - Ordena a lista
lista = [5, 3, 7, 10, 8]
lista.sort(reverse=True)
print("sort()", lista)

# clear() - Remove todos os elementos da lista
lista = [5, 3, 7, 10, 8]
lista.clear()
print("clear()", lista)

# copy() - Cria uma cópia da lista
lista = [5, 3, 7, 10, 8]
lista2 = lista.copy() # lista[:]
print("copy()", lista2)

# count() - Retorna o número de vezes que um elemento aparece na lista
lista = [1, 2, 3, 3, 3, 4, 5, 3, 3, 1]
qtd = lista.count(3)
print("count()", qtd)

# index() - Retorna o índice da primeira ocorrência do elemento
lista = [1, 2, 3, 3, 3, 4, 5, 3, 3, 1]
ind = lista.index(3)
print("index()", ind)

# extend() - Adiciona elementos de uma lista ao final de outra
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista1.extend(lista2)
print("extend()", lista1)