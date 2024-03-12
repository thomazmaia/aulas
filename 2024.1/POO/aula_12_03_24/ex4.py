# Classe CalculadoraV1
# • Atributos: val1 (float), val2 (float)
# • Métodos: somar(), subtrair(), multiplicar(), dividir()

class CalculadoraV1:
    def __init__(self, v1 : float, v2 : float) -> None:
        self.val1 = v1
        self.val2 = v2

    def somar(self):
        res = self.val1 + self.val2
        print(f"Soma = {res}")

    def subtrair(self):
        res = self.val1 - self.val2
        print(f"Subtração = {res}")

    def multiplicar(self):
        res = self.val1 * self.val2
        print(f"Multiplicação = {res}")

    def dividir(self):
        res = self.val1 / self.val2
        print(f"Divisão = {res}")


C = CalculadoraV1(3, 5)
C.somar()
C.subtrair()
C.multiplicar()
C.dividir()