# Crie uma lista de números inteiros. Em seguida, pergunte ao usuário por um número. Se o número estiver na lista, modifique-o para zero; caso contrário, exiba uma mensagem informando que o número não está na lista.

L = [2, 4, 6, 8, 10]

numero = int(input("Digite um número: "))

flag = False
for i in range(len(L)):
    if numero == L[i]:
        L[i] = 0
        flag = True

if flag == False:
    print("O número não está na lista")

print(L)