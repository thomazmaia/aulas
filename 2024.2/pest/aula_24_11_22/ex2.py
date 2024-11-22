# Crie 4 funções diferentes. Cada função irá receber 2 parâmetros e irá retornar um valor de um cálculo.
# As 4 funções são:
# - somar(num1, num2): deve retornar a soma de num1 com num2
# - subtrair(num1, num2): deve retornar a subtração de num1 por num2
# - multiplicar(num1, num2): deve retornar o produto de num1 por num2
# - dividir(num1, num2): deve retornar a divisão de num1 por num2
# Crie um programa para testar as funções.

def somar(num1 : float, num2 : float):
    resultado = num1 + num2
    return resultado

def subtrair(num1 : float, num2 : float):
    res = num1 - num2
    return res

def multiplicar(num1 : float, num2 : float):
    return num1 * num2

def dividir(num1 : float, num2: float):
    return num1/num2

resultado_soma = somar(2.5, 1.25)
resultado_subtracao = subtrair(20, 25)
resultado_multiplicaco = multiplicar(2.5, 4)
resultado_divisao = dividir(100, 25)

print(resultado_soma)
print(resultado_subtracao)
print(resultado_multiplicaco)
print(resultado_divisao)