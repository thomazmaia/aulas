# Crie um programa para calcular o IMC (Índice de Massa Corporal) de
# uma pessoa com base em seu peso (em quilogramas) e altura (em metros).
# Após calcular o IMC, classifique a pessoa em uma das categorias:
# "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obeso".
# Use estruturas condicionais aninhadas.

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"IMC = {imc}. Baixo peso")
else:
    if imc >= 18.5 and imc < 24.99:
        print(f"IMC = {imc}. Peso normal")
    else:
        if imc >= 24.99 and imc < 29.99:
            print(f"IMC = {imc}. Sobrepeso")
        else:
            print(f"IMC = {imc}. Obeso")
