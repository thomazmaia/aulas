# Crie uma lista de números inteiros e, em seguida, peça ao usuário para inserir um número e uma posição. O programa deve usar o método insert para inserir o número na posição especificada e, em seguida, imprimir a lista resultante.

lista = [1, 2, 3, 4, 5]

numero = int(input("Digite um numero: "))
posicao = int(input("Digite uma posicao: "))

lista.insert(posicao-1, numero)

print(lista)