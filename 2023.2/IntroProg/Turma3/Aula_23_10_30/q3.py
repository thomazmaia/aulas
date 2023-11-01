peso_kg = float(input("Peso em kg: "))
altura_cm = float(input("Altura em cm: "))

altura_m = altura_cm / 100
IMC = peso_kg / altura_m**2

if IMC < 18.5:
    print(f"Seu imc é de {IMC} e você está com baixo peso")
elif IMC >= 18.5 and IMC <= 24.99:
    print(f"Seu imc é de {IMC} e você está normal")
elif IMC >= 25 and IMC <= 29.99:
    print(f"Seu imc é de {IMC} e você está com sobrepeso")
else:
    print(f"Seu imc é de {IMC} e você está obeso")
