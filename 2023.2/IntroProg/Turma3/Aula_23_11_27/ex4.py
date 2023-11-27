N = int(input(""))

contador = 0

if N > 0:
    while contador <= N:
        print(contador)
        contador += 1
elif N < 0:
    while contador >= N:
        print(contador)
        contador -= 1