# MÉTODOS DE ADIÇÃO DE ELEMENTOS NA LISTA
# 1) append() - adiciona o elemento ao FINAL da lista
# 2) insert() - adiciona o elemento em uma posição ESPECÍFICA

L = [1, 2, 3]

print(L)
L.append('A')
L.append(3.14)
L.append('uva')
print(L)

L.insert(3, 'X')
print(L)