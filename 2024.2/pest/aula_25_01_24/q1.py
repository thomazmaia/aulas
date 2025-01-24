L = []

numero = 1
while numero != 0:
    numero = int(input("Digite um número ou 0 para sair: "))
    if numero != 0:
        L.append(numero)

print(L)