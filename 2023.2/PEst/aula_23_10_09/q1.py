# Escreva um programa que peça ao usuário para inserir
# números inteiros em uma lista até que ele digite '0'.
# Em seguida, o programa deve imprimir a lista resultante.

lista = []

while True:
    num = int(input("Número: "))
    if num == 0:
        break
    lista.append(num)

print(lista)
