# Crie uma lista de números inteiros. Em seguida, pergunte ao usuário por um número. Se o número estiver na lista, modifique-o para zero; caso contrário, exiba uma mensagem informando que o número não está na lista.

lista = [1, 2, 8, 15, -8, 50, 2, 20, 22, 18, 2, 10]

numero = int(input("Digite um número: "))

print("Lista antes: ")
print(lista)

for i in range(len(lista)):
    if numero == lista[i]:
        lista[i] = 0

print("Lista depois: ")
print(lista)