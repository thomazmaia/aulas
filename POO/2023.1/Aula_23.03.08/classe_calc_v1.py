class CalculadoraV1:
    def __init__(self, v1, v2):
        self.val1 = v1
        self.val2 = v2

    def somar(self):
        print(f"{self.val1} + {self.val2} = {self.val1+self.val2}")

    def subtrair(self):
        print(f"{self.val1} - {self.val2} = {self.val1-self.val2}")

    def multiplicar(self):
        print(f"{self.val1} * {self.val2} = {self.val1*self.val2}")

    def dividir(self):
        if self.val2 != 0:
            print(f"{self.val1} / {self.val2} = {self.val1/self.val2}")

calc = CalculadoraV1(10, 5)
calc.somar()
calc.subtrair()
calc.multiplicar()
calc.dividir()

operacoes = CalculadoraV1(2, 0)
operacoes.somar()
operacoes.subtrair()
operacoes.multiplicar()
operacoes.dividir()