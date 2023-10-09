# Crie um programa para calcular o IMC (Índice de Massa Corporal) de uma pessoa
# com base em seu peso (em quilogramas) e altura (em metros). Após calcular o IMC,
# classifique a pessoa em uma das categorias:
# "Abaixo do peso",
# "Peso normal",
# "Sobrepeso" ou
# "Obeso".
# Use estruturas condicionais aninhadas.

peso = float(input("Peso (kg): "))
altura = float(input("Algura (m): "))

IMC = (peso) / (altura**2)

if IMC <= 18.5:
    print(f"IMC = {IMC}")
    print("Abaixo do peso")
else:
    if IMC <= 24.99:
        print(f"IMC = {IMC}")
        print("Peso normal")
    else:
        if IMC <= 29.99:
            print(f"IMC = {IMC}")
            print("Sobrepeso")
        else:
            print(f"IMC = {IMC}")
            print("Obeso")
