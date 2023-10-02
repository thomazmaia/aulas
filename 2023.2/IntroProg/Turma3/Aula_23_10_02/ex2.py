# Leia um número inteiro e diga a qual dia esse número corresponde.
# Caso não corresponda a nenhum dia, escreva "Dia inválido"
# OBS: 1 é domingo, 2 é segunda, 3 é terça...

num = int(input("Digite um número: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda")
elif num == 3:
    print("Terça")
elif num == 4:
    print("Quarta")
elif num == 5:
    print("Quinta")
elif num == 6:
    print("Sexta")
elif num == 7:
    print("Sábado")
else:
    print("Dia inválido")
