N = 33

palpite = int(input("Digite um número: "))

tentativa = 3

while palpite != N:
    tentativa = tentativa - 1
    if tentativa == 0:
        print("Tentativas acabaram!")
        break
    if palpite > N:
        palpite = int(input("Errado! Digite outro número MENOR: "))
    elif palpite < N:
        palpite = int(input("Errado! Digite outro número MAIOR: "))

if tentativa != 0:
    print("Acertou!")