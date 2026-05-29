# MÉTODOS DE ADIÇÃO DE ELEMENTOS NA LISTA
# 1) append() - adiciona o elemento ao FINAL da lista
# 2) insert() - adiciona o elemento em uma posição específica

L = [1, 2, 3]
print(L)
L.append(4)
L.append(5)
L.append(6)
print(L) # [1, 2, 3, 4, 5, 6]

L.insert(2, 'oi')
L.insert(5, 'tchau')
print(L) # [1, 2, 'oi', 3, 4, 'tchau', 5, 6]