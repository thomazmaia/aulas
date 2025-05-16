# OPERAÇÕES COM LISTAS
# Remoção
# 1) pop(): Remove o último elemento da lista (caso não seja passado nada como argumento) e o retorna ou remove o elemento no índice passado por argumento.
# 2) remove(): Remove o primeiro elemento da lista que tem o valor especificado.
# OBS: Antes de remover, SEMPRE verifique se o elemento EXISTE na lista
# Ex:

L = [4, 5, 8, 10, 4, 6, 7, 4, 0]

print(f"Antes: {L}")
L.pop() # Remove o último elemento da lista
L.pop(2) # Remove o elemento cujo índice é 2 (terceiro elemento)
L.pop(5) # Remove o elemento cujo índice é 5 (sexto elemento)
print(f"Depois do pop: {L}")

if 4 in L:
    L.remove(4) # Remove o primeiro elemento '4'
if 4 in L:
    L.remove(4) # Remove o primeiro elemento '4'
if 4 in L:
    L.remove(4) # Remove o primeiro elemento '4'
if 4 in L:
    L.remove(4) # Remove o primeiro elemento '4'
print(f"Depois do remove: {L}")

