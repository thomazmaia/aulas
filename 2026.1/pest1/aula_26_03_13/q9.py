inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for N in range(inicio, fim):
    # Passo 1: contar a quantidade de dígitos
    temp = N
    qtd = 0
    while temp > 0:
        temp = temp // 10
        qtd += 1

    # print(f"A qtd de dígitos é {qtd}")

    temp = N
    soma = 0
    while temp > 0:
        digito = temp % 10
        soma += digito ** qtd
        temp = temp // 10 

    # print(f"A soma foi de {soma}")

    if soma == N:
        print(f"O número {N} é narcisista")
    else:
        print(f"O número {N} NÃO é narcisista")