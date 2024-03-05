# Crie um programa para verificar se um número é primo ou não. Utilize o comando for.

N = int(input("Digite o número: "))
contador_de_divisoes = 0

for i in range(1, N+1):
    if N % i == 0: # verifica se é inteiro
        contador_de_divisoes += 1

if contador_de_divisoes == 2:
    print("Primo")
else:
    print("NÃO Primo")


# N/(1 -> N)
# SE ESSA DIVISÃO É INTEIRA
# QUANTAS DIVISÕES INTEIRAS ACONTECERAM
# SE ACONTECER APENAS 2, É PRIMO

# 6/1 = 6 (ok)
# 6/2 = 3 (ok)
# 6/3 = 2 (ok)
# 6/4 = 1.5 (x)
# 6/5 = 1.2 (x)
# 6/6 = 1 (ok)