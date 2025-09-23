# Crie uma função chamada calculadora que aceita três parâmetros: num1, num2 e operacao. A operação pode ser "soma", "subtracao", "multiplicacao" ou "divisao". A função deve retornar o resultado da operação.

def calculadora(num1 : float, num2 : float, operacao : str) -> float:
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        return num1/num2
    

valor = calculadora(10, 20, "soma")
print(valor)
valor = calculadora(5, 2, "subtracao")
print(valor)
valor = calculadora(100, 2.5, "divisao")
print(valor)
valor = calculadora(3.5, 10, "multiplicacao")
print(valor)