N = int(input("Digite um número: "))

if N > 0:
    contador = N
    while contador >= 0:
        print(contador)
        contador -= 1
elif N < 0:
    contador = N
    while contador <= 0:
        print(contador)
        contador += 1