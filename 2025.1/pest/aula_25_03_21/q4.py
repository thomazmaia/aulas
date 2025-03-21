N = int(input("Digite um número: "))
# N = 10

contador = 1

while contador <= N:
    if(N % contador == 0):
        print(f"{contador} é divisor")
    contador = contador + 1