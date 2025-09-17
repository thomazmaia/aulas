def calculadora(num1 : float, num2 : float, operacao : str) -> float:
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "divisao":
        resultado = num1 / num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    
    return resultado


res = calculadora(3.5, 10, "soma")
print(res)
res = calculadora(3.5, 10, "subtracao")
print(res)
res = calculadora(3.5, 10, "divisao")
print(res)
res = calculadora(3.5, 10, "multiplicacao")
print(res)