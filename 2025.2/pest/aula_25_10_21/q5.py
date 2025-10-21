# Crie uma lista vazia com cinco posições e, em seguida, peça ao usuário para inserir cinco nomes. Armazene esses nomes na lista e, por fim, exiba a lista completa.

lista = ['', '', '', '', '']

print("Lista antes:")
print(lista)

for i in range(5):
    nome = input("Digite um nome: ")
    lista[i] = nome

print("Lista depois:")
print(lista)