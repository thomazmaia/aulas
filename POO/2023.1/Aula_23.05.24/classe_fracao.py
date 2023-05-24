class Fracao:
    def __init__(self, num, den) -> None:
        self.numerador = num
        self.denominador = den

    def val(self):
        try:
            return float(self.numerador) / float(self.denominador)
        except ZeroDivisionError:
            return "Impossível"

    def __str__(self) -> str:
        res = self.val()
        return f"{self.numerador}/{self.denominador} = {res}"


F = Fracao(3, 0)

num = input("Digite um numero: ")
F2 = Fracao(5, num)
print(F2)
