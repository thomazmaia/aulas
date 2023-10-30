peso_kg = float(input("Digite seu peso em kg: "))
altura_cm = int(input("Digite sua altura em cm: "))

altura_m = altura_cm / 100

IMC = peso_kg / (altura_m**2)

if IMC <= 18.5:
    print(f"Seu IMC é de {IMC} e você está com Baixo peso")
elif IMC > 18.5 and IMC <= 24.99:
    print(f"Seu IMC é de {IMC} e você está Normal")
elif IMC >= 25 and IMC <= 29.99:
    print(f"Seu IMC é de {IMC} e você está com Sobrepeso")
else:
    print(f"Seu IMC é de {IMC} e você está Obeso")
