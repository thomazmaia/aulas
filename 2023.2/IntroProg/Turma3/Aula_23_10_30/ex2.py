# Leia um número inteiro de dois dígitos e verifique se os
# dígitos são iguais ou diferentes.
# Ex: 22 -> Os dígitos são iguais
# Ex: 13 -> Os dígitos são diferentes

numero = int(input("Número: "))

unidade = numero % 10
dezena = numero // 10

if unidade == dezena:
    print("Os dígitos são iguais")
else:
    print("Os dígitos são diferentes")
