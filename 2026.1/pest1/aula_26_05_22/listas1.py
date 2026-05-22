# LISTAS
# São estruturas de dados que armazenam valores em elementos acessados por um índice. Uma lista pode conter zero ou mais elementos e o tamanho da lista é igual a quantidade de elementos que ela contém
# Ex:
# L = [1, 2, 3]
# L[0] é o elemento 1
# L2 = [] -> Lista vazia

# Diferença entre listas e strings: listas são MUTÁVEIS
L = [1, 2, 3]

print(L)
L[0] = 99
print(L)

# Listas com dados variados
L = [1, 2, 3, 4.5, 6.73, 'A', 'B', 'Abacaxi']
print(L)
print(len(L))

# Percorrendo elementos da lista:
L = [1, 2, 3, 4.5, 6.73, 'A', 'B', 'Abacaxi']

for i in range(len(L)):
    print(L[i])

for item in L:
    print(item)