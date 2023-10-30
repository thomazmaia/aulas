# Leia um número inteiro de 2 dígitos e
# informe se os dígitos são iguais ou não.
# Ex: 22 - os dígitos são iguais
# Ex: 12 - os dígitos não são iguais
# Use os novos operadores MAS NÃO APENAS eles

numero = int(input("Número: "))

dig1 = numero % 10
dig2 = numero // 10
print(f"{dig1}{dig2}")

if dig1 == dig2:
    print("Os dígitos são iguais")
else:
    print("Os dígitos NÃO são iguais")
