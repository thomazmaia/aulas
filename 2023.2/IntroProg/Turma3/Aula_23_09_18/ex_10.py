# Calculadora de IMC (Índice de Massa Corporal): Solicite ao usuário que
# insira seu peso (em kg) e altura (em metros) e calcule o IMC.
# OBS: procure como é o cálculo do IMC.

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

print(f"IMC = {imc}")
