# Crie uma função chamada calculadora que aceita três parâmetros: num1, num2 e operacao. A operação pode ser "soma", "subtracao", "multiplicacao" ou "divisao". A função deve retornar o resultado da operação.

def calculadora(num1 : float, num2 : float, operacao : str):
    res = 0
    if operacao == "soma":
        res = num1 + num2
    elif operacao == "subtracao":
        res = num1 - num2
    elif operacao == "multiplicacao":
        res = num1 * num1
    elif operacao == "divisao":
        res = num1 / num2
    return res


N1 = float(input("Digite o número: "))
N2 = float(input("Digite o número: "))
op = input("Escreva a operação (sem acentos): ")

print(calculadora(N1, N2, op))