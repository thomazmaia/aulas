# 1. Crie uma função chamada "somar" que recebe dois valores numéricos e escreve a soma desses dois valoes.

def somar(param1 : float, param2 : float):
    print(param1 + param2)

somar(5, 8)

# 2. Crie uma função chamada "subtrair" que recebe dois valores numéricos e RETORNA a diferença (subtração) entre esses dois valores.

def subtrair(a : float, b : float):
    resultado = a - b
    return resultado

aux = subtrair(10, 3)
print(aux)

# 3. Crie uma função chamada "calculadora" que recebe três parâmetros: "num1", "num2" e "operacao". "num1" e "num2" são dois valores numéricos e "operacao" é uma string. Realize a operação solicitada pelo usuário e retorne o valor para o programa principal.
# Ex de uso:
#  calculadora(3, 5, "somar") deve retornar o valor "8"
#  calculadora(3, 5, "subtrair") deve retornar o valor "-2"

def calculadora(num1 : float, num2 : float, operacao : str):
    res = 0
    if operacao == "somar":
        res = num1 + num2
    elif operacao == "subtrair":
        res = num1 - num2
    return res

print(calculadora(3, 5, "soma"))
print(calculadora(3, 5, "subtrair"))