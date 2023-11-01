# Crie um programa para somar horas. Seu programa deve ler a
# quantidade de horas atual através de um número inteiro e deve
# somar com outro número inteiro lido pelo usuário. Ao final,
# mostre a hora resultante em um relógio de 12h.
# Ex: 10h + 10h = 20h = 8h

hora = int(input("Digite a hora: "))
soma = int(input("Digite a hora: "))

res = hora + soma

print(res%12)

# if res > 12:
#     print(res-12)
# else:
#     print(res)