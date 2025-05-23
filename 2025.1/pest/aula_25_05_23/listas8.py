# LISTAS ANINHADAS - LISTAS DENTRO DE LISTAS 
#              ou MATRIZES

L =[[1, 2], ['a', 2.5]]

print(L[0]) # Lista [1, 2]
print(L[1]) # Lista ['a', 2.5]

print(L[1][0]) # Elemento 'a'
print(L[0][1]) # Elemento 2

# Percorrendo e acessando os elementos
print(20*'-')
L = [['a', 'b', 'c'],
     [10, 20, 30],
     ['uva', 'maçã', 'limão']]

print(len(L))
for elemento in L:
    # print(elemento)
    for item in elemento:
        print(item)
print(20*'-')

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j])
print(20*'-')
print(L[1][2])