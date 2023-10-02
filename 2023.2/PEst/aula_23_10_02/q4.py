# Crie uma lista de números inteiros. Em seguida, pergunte ao
# usuário por um número. Se o número estiver na lista,
# modifique-o para zero; caso contrário, exiba uma mensagem
# informando que o número não está na lista.

L = [6, 5, 3, 9, 8, 10]

print(L)
numero = int(input("Número: "))

flag = False

for indice in range(len(L)):
    if L[indice] == numero:
        L[indice] = 0
        flag = True

if flag:
    print(f"O {numero} está na lista")
else:
    print(f"O {numero} NÃO está na lista")

print(L)
