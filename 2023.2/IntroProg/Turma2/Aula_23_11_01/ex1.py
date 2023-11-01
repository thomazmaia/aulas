# Cria um programa para ler um número inteiro de 3 dígitos e 
# escreva a soma desses dígitos.
# Ex: numero = 375 -> Soma = 15

numero = int(input("Número: "))

dig3 = numero % 10
numero = (numero - dig3)/10 # numero = numero // 10

dig2 = numero % 10
numero = (numero - dig2)/10 # numero = numero // 10

dig1 = numero % 10
numero = (numero - dig1)/10 # numero = numero // 10

print(dig1 + dig2 + dig3)
