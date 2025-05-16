# 1. Escreva um programa que peça ao usuário para inserir números inteiros em uma lista até que ele digite `0`. Em seguida, o programa deve imprimir a lista resultante. 

L = list() # L = []

numero = 1
while numero != 0:
    numero = int(input("Digite um número ou 0 para sair: "))
    L.append(numero)

L.pop()
print(L)