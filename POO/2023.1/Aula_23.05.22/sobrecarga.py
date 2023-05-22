class Fracao:
    def __init__(self, num, den) -> None:
        self.num = num
        self.den = den

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __mul__(self, val):
        novo_num = self.num * val.num
        novo_den = self.den * val.den
        return Fracao(novo_num, novo_den)


f1 = Fracao(1, 2)
f2 = Fracao(3, 4)
print(f1)
print(f2)
print(f1 * f2)
