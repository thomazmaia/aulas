

def calc(n1, n2, operacao):
    if operacao == "soma":
        res = n1 + n2
        return res
    elif operacao == "produto":
        res = n1 * n2
        return res
    elif operacao == "divisao":
        res = n1 / n2
        return res
    elif operacao == "subtracao":
        res = n1 - n2
        return res


# (4 + 3) x 2
x = calc(4, 3, "soma")
eq = calc(x, 2, "produto")

print(eq)
