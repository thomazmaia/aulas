def soma(num1 : int, num2 : int):
    soma = num1 + num2
    return soma

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

resultado = soma(numero1, numero2)

print(f"A soma é {resultado}")