# Crie um programa para ler um número inteiro representado as
# horas do horário atual. Leia outro número inteiro e some
# a essa hora. Dê o resultado como um relógio de ponteiro.
# Ex: 7 + 7 = 2 (14h)
#     10 + 5 = 3 (15h)

hora = int(input("Hora 1: "))
soma = int(input("Hora 2: "))

print((hora+soma)%12)
