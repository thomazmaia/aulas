N = int(input("Digite um número: "))

saida = 0

while N > 0:
    ultimo_digito = N % 10
    saida = saida * 10 + ultimo_digito
    N = N // 10

print(saida)