N = int(input("Digite um número de 5 dígitos: "))
#N = 35442

# Primeira parte:
d1 = N % 10 # Unidade: 2
N = N // 10 # 3544
d2 = N % 10 # Dezena: 4
N = N // 10 # 354
d3 = N % 10 # Centena: 4
N = N // 10 # 35
d4 = N % 10 # Milhar: 5
N = N // 10 # 3
d5 = N % 10 # Dezena de milhar: 3
N = N // 10 # 0

# Segunda parte:
if (d1 == d2) or (d1 == d3) or (d1 == d4) or (d1 == d5):
    print("Digito 1 se repete")
if (d2 == d3) or (d2 == d4) or (d2 == d5):
    print("Digito 2 se repete")
if (d3 == d4) or (d3 == d5):
    print("Digito 3 se repete")
if (d4 == d5):
    print("Digito 4 se repete")