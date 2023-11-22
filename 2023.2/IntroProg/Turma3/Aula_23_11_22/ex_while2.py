fim = int(input("Valor: "))

contador = 1

while contador <= fim:
    if contador % 2 == 1: # é impar?
        print(contador)
    contador = contador+1