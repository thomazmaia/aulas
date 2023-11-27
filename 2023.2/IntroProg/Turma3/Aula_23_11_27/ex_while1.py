# Criem um acumulador que mostre a soma de todos os números de X a N. X e N lidos pelo usuário.
X = int(input("Digite X: "))
N = int(input("Digite N: "))

contador = X
acumulador = 0

while contador <= N:
    acumulador += contador  # acumulador + contador    
    contador += 1           # contador + 1

print(acumulador)
