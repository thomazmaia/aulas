# MÉTODOS DE LISTAS
# Métodos de ADIÇÃO de elementos
# - append() adiciona um elemento ao final da lista
# - insert() adiciona um elemento em um local (índice) específico


L = [1, 2, 3]

print(L)            # Printa lista antes
L.append(199)       # Adiciona 199 ao final da lista
print(L)            # Printa lista depois
L.append("uva")     # Adiciona "uva" ao final da lista
L.append(1.5)       # Adiciona 1.5 ao final da lista
L.append(True)      # Adiciona True ao final da lista
print(L)            # Printa lista depois

L.insert(3, "abacaxi") # Insere o elemento "abacaxi" no índice 3
print(L)            # Printa lista depois


# Métodos de REMOÇÃO de elementos
# - pop() apaga (e retorna) um elemento de um índice específico
# - remove() apaga um elemento específico (primeira ocorrência)

L = [1, 2, 3, 'abacaxi', 199, 'uva', 1.5, True]

print(L)            # Printa a lista antes
L.pop(3)            # Remove o elemento do índice 3
print(L)            # Printa a lista depois
L.pop(3)            # Remove o elemento do índice 3
print(L)            # Printa a lista depois
L.pop(3)            # Remove o elemento do índice 3
print(L)            # Printa a lista depois
#L.pop(10)           # Erro

L = ['a', 'b', 2, 'c', 2, 4, 19, 2, 'oi']
print(L)            # Printa a lista antes
L.remove('a')       # Remove o elemento 'a'
print(L)            # Printa a lista depois
L.remove(2)         # Remove o primeiro elemento 2
print(L)            # Printa a lista depois
L.remove(2)         # Remove o primeiro elemento 2 (do que sobraram)
print(L)            # Printa a lista depois


# VERIFICAR A EXISTÊNCIA DE UM ELEMENTO
# O operador 'in' verifica se um elemento está na lista
L = [0, 1, 2, 3, 4, 6, 7, 8, 9]

if 5 in L:
    print("O 5 está na lista")
else:
    print("O 5 não está na lista")