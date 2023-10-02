# Leia um número inteiro e diga a qual dia esse número corresponde.
# Caso não corresponda a nenhum dia, escreva "Dia inválido"

dia = int(input("Número: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido")
