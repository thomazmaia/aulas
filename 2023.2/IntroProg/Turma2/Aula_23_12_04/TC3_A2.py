menor = 999999
maior = -999999

acumulador = 0

contador = 1
while contador <= 5:
    nota = float(input(f"Nota {contador}: "))
    acumulador += nota
    if nota < menor:
        menor = nota
    if nota > maior:
        maior = nota
    contador += 1

soma = acumulador - maior - menor
mp = soma/3

print(f"Média Parcial (MP): {mp}")

if mp < 3:
    print("Reprovado direto")
elif mp >= 6:
    print("Aprovado direto")
else:
    print("Recuperação")
    nota_recuperacao = float(input("Nota de recuperação: "))
    mf = (mp + nota_recuperacao)/2
    print(f"Média Final (MF): {mf}")
    if mf >= 5:
        print("Aprovado")
    else:
        print("Reprovado")