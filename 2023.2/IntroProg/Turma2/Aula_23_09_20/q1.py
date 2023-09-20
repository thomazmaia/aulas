# Crie um programa que pede ao usuário sua idade e verifica
# se ele é menor de idade (menor que 18 anos) ou maior de idade
# (18 anos ou mais).

idade = int(input("Idade: "))

if idade < 18:
    print("Menor de idade")
if idade >= 18:
    print("Maior de idade")
