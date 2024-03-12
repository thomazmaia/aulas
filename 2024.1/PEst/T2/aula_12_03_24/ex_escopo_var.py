def eh_primo(N : int):
    contador_de_divisoes = 0
    global contador_de_numeros_primos

    for i in range(1, N+1):
        if N % i == 0: # verifica se é inteiro
            contador_de_divisoes += 1

    if contador_de_divisoes == 2:
        contador_de_numeros_primos += 1
        return True
    else:
        return False

contador_de_numeros_primos = 0

while True:
    N = int(input("Digite um número ou zero pra sair: "))
    if N == 0:
        break
    eh_primo(N)
        

print(f"Você digitou {contador_de_numeros_primos} números primos")

