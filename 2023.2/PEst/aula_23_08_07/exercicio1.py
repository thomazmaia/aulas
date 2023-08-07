cont = 1
soma = 0

while cont < 10:
    if cont % 3 == 0:
        soma = soma + cont
    cont = cont + 1

print(f"A soma dos números divisíveis por 3 é {soma}")
