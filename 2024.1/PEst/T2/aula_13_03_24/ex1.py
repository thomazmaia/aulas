def calculadora(n1 : float, n2: float, op : str):
    if op == "soma":
        return n1 + n2
    elif op == "subtracao":
        return n1 - n2
    elif op == "multiplicacao":
        return n1 * n2
    elif op == "divisao":
        return n1 / n2
    
print(calculadora(3, 5, "soma"))
print(calculadora(10, 2, "divisao"))