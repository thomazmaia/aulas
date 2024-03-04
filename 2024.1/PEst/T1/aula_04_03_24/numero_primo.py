# Crie um programa para verificar se um número é primo ou não. Utilize o comando for.

N = int(input("Digite um número: "))
contador_de_divisoes = 0

for i in range (1, N+1):
    if N % i == 0:
        contador_de_divisoes += 1

if contador_de_divisoes == 2:
    print("Número primo")
else:
    print("NÃO é primo")

# N % (1 -> N) == 0:
#     se acontece mais de duas vezes

# 7/1 = 7 (ok)
# 7/2 = (x)
# 7/3 = (x)
# 7/4 = (x)
# 7/5 = (x)
# 7/6 = (x)
# 7/7 = 1 (ok)