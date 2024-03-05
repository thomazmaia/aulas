# Crie um código em Python que calcule a soma dos números primos de 1 a 100 usando o comando for.

def eh_primo(N):
    contador_de_divisoes = 0

    for i in range(1, N+1):
        if N % i == 0: # verifica se é inteiro
            contador_de_divisoes += 1

    if contador_de_divisoes == 2:
        return True
    else:
        return False


acumulador = 0

for i in range (1, 11):
    if eh_primo(i):
        acumulador += i

print(acumulador)