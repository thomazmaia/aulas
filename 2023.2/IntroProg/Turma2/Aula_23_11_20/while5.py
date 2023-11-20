# Crie um programa que peça um número inteiro positivo N do usuário e imprima a tabuada de multiplicar desse número usando while.

N = int(input("Número: "))

contador = 0

while contador <= 10:
    print(f"{contador} x {N} = {contador * N}")
    contador = contador + 1