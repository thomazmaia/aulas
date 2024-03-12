# Classe CalculadoraV2
# • Atributos: -
# • Métodos: somar(float, float), subtrair(float, float), multiplicar(float, float), dividir(float, float)

class CalculadoraV2:
    def __init__(self) -> None:
        pass

    def somar(self, v1 : float, v2 : float):
        res = v1 + v2
        print(f"Soma = {res}")

    def subtrair(self, v1 : float, v2 : float):
        res = v1 - v2
        print(f"Subtração = {res}")

    def multiplicar(self, v1 : float, v2 : float):
        res = v1 * v2
        print(f"Multiplicação = {res}")

    def dividir(self, v1 : float, v2 : float):
        res = v1 / v2
        print(f"Divisão = {res}")


C = CalculadoraV2()
C.somar(10, 20)
C.subtrair(5, 2)
C.multiplicar(3, 6)
C.dividir(125, 5)