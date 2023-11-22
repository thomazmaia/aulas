# 7. Crie um programa que peça um número ao usuário e imprima a tabuada desse número usando um loop "while".

N = int(input("Número: "))

contador = 0

while contador <= 10:
    res = contador*N
    print(f"{contador} x {N} = {res}")
    contador += 1