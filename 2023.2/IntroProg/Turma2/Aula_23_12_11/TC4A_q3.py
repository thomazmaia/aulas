# 3! = 3 x 2 x 1
# 5! = 5 x 4 x 3 x 2 x 1
# 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1

N_original = int(input("Digite um número: "))
N = N_original
multiplicacao = 1

while N >= 1:
    multiplicacao = multiplicacao * N
    N = N - 1

print(f"Fatorial de {N_original} = {multiplicacao}")