# Crie uma função chamada calculadora que aceita três parâmetros: num1, num2 e operacao. A operação pode ser "soma", "subtracao", "multiplicacao" ou "divisao". A função deve retornar o resultado da operação.

def calculadora(num1 : float, num2 : float, operacao : str):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        return num1 / num2


N1 = float(input("Digite um número: "))
N2 = float(input("Digite um número: "))
op = input("Opção: ")

res = calculadora(N1, N2, op)
print(res)