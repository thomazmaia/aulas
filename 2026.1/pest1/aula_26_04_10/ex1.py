# Crie uma função que receba como parâmetros dois números e uma string com o nome de uma operação matemática. A sua função deve retornar o resultado da operação sobre os dois números.
# Ex:
# calcula(3, 8, "multiplicacao") -> 24

def calcula(numero1, numero2, operacao):
    if operacao == "soma":
        return (numero1 + numero2)
    elif operacao == "subtracao":
        return (numero1 - numero2)
    elif operacao == "divisao":
        return (numero1 / numero2)
    elif operacao == "multiplicacao":
        return (numero1 * numero2)

res = calcula(2, 5, "soma")

if res is not None:
    print(res)
else:
    print("Deu algum erro ai...")