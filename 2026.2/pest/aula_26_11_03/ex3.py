# Crie uma função que receba dois números e uma string representando a operação. Realize a operação e mostre o resultado.
# Ex: dados (3, 5, "soma") o resultado deve ser 8
#     dados (2, 3, "produto") o resultado deve ser 6
#     dados (10, 2, "divisao") o resultado deve ser 5
#     dados (7, 4, "subtracao") o resultado deve ser 3

def calculos(n1, n2, operacao):
    if operacao == "soma":
        res = n1 + n2
        print(f"{n1} + {n2} = {res}")
    elif operacao == "produto":
        res = n1 * n2
        print(f"{n1} * {n2} = {res}")
    elif operacao == "divisao":
        res = n1 / n2
        print(f"{n1} / {n2} = {res}")
    elif operacao == "subtracao":
        res = n1 - n2
        print(f"{n1} - {n2} = {res}")


calculos(3, 5, "soma")
calculos(2, 3, "produto")
calculos(10, 2, "divisao")
calculos(7, 4, "subtracao")


calculos(87, 32, "produto")
calculos(47, 8, "divisao")