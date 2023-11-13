# Escreva um programa que verifique se um número inteiro de 5 dígitos
# é palíndromo. Um número é palíndromo se ele continua o mesmo número 
# caso seus dígitos sejam invertidos.

num = int(input("Digite um número: "))

# ex: 16461
#     ABCDE

E = num % 10
num = num // 10
D = num % 10
num = num // 10
C = num % 10
num = num // 10
B = num % 10
num = num // 10
A = num % 10

if E == A and D == B:
    print("Palíndromo")
else:
    print("Não é palíndromo")