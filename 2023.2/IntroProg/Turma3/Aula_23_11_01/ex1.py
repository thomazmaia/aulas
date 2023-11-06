# Crie um programa para ler um número inteiro de 3 dígitos e
# imprima a soma desses 3 dígitos.
# Ex: 375 -> Soma = 15
# Ex: 123 -> Soma = 6

N = int(input("Número: "))

u = N%10
N = N//10

d = N%10
N = N//10

c = N%10
N = N//10

print(u + d + c)