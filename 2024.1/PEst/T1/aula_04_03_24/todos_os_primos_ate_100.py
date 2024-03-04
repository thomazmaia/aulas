def eh_primo(i):
    N = i
    contador_de_divisoes = 0

    for i in range (1, N+1):
        if N % i == 0:
            contador_de_divisoes += 1

    if contador_de_divisoes == 2:
        return True
    else:
        return False


acumulador = 0

print("E ai galera?!")

print(acumulador)