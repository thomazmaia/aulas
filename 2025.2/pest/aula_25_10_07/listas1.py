# DEFINIÇÃO
# Listas são um tipo de variável que permitem o armazenamento de vários valores ao mesmo tempo. Esses valores são acessados por um índice que começa de zero.
# Ex:
L = [2, 3.1, 'a', 'uva', -1]
print(L)

# Acessando elementos
# Para acessar elementos você precisa colocar o índice dentro dos colchetes da variável da lista
# Ex:
print(L[2]) # 'a'
print(L[4]) # -1

# Modificando elementos
# Para modificar elementos basta acessar o elemento e modificar seu conteúdo
print(f"Antes: {L[0]}") # 2
L[0] = 'abacaxi'
print(f"Depois: {L[0]}") # 'abacaxi'
