# OPERAÇÕES COM LISTAS
# Adição
# 1) append(): Adiciona um elemento ao final da lista.
# 2) insert(): Adiciona um elemento em uma posição específica da lista.
# Ex:
L = [3, 5, 10, 4, 3, 8, 5, 0]

print(f"Antes: {L}")
L.append(10)
L.append('a')
L.append('uva')
print(f"Depois do append: {L}")

# L.insert(10) # Erro
L.insert(0, 10) # Insere 10 na primeira posição (índice 0)
L.insert(5, 'abacaxi')
print(f"Depois do insert: {L}")