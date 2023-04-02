class CalculadoraV2:
    def __init__(self) -> None:
        pass

    def somar(self, val1, val2):
        print(f"{val1} + {val2} = {val1+val2}")

    def subtrair(self, val1, val2):
        print(f"{val1} - {val2} = {val1-val2}")

    def multiplicar(self, val1, val2):
        print(f"{val1} * {val2} = {val1*val2}")

    def dividir(self, val1, val2):
        if val2 != 0:
            print(f"{val1} / {val2} = {val1/val2}")

calc = CalculadoraV2()
calc.somar(5, 3)
calc.subtrair(10, 3)
calc.subtrair(0, 3)
calc.dividir(4, 2)