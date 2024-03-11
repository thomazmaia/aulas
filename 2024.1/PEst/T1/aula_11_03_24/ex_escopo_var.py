def eh_primo(num : int):
    global contador
    contador_de_divisoes = 0

    for i in range (1, num+1):
        if num % i == 0:
            contador_de_divisoes += 1

    if contador_de_divisoes == 2:
        print(contador)
        contador += 1
        return True
    return False


contador = 0
while True:
    N = int(input("Digite um número: "))
    if eh_primo(N):
        print(f"{N} é primo")
    if N == 0:
        break

print(f"{contador} números primos")