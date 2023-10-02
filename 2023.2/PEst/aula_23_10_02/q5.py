# Crie uma lista vazia com cinco posições e, em seguida, peça ao usuário
# para inserir cinco nomes. Armazene esses nomes na lista e, por fim, exiba
# a lista completa.

L = [0, 0, 0, 0, 0]

for indice in range(len(L)):
    L[indice] = input("Nome: ")

print(L)
