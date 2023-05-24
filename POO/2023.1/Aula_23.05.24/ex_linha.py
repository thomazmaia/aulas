from math import sqrt


class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, ponto):
        if self.x == ponto.x and self.y == ponto.y:
            return True
        return False


class Linha:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.comprimento = self.calc_comprimento()

    def calc_comprimento(self):
        p1x = self.p1.x
        p1y = self.p1.y
        p2x = self.p2.x
        p2y = self.p2.y
        return sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)

    def __gt__(self, linha):
        return self.comprimento > linha.comprimento

    def __lt__(self, linha):
        return self.comprimento < linha.comprimento

    def __ge__(self, linha):
        return self.comprimento >= linha.comprimento

    def __le__(self, linha):
        return self.comprimento <= linha.comprimento

    def __eq__(self, linha):
        return self.comprimento == linha.comprimento


A = Ponto(0, 0)
B = Ponto(10, 10)
L1 = Linha(A, B)
L2 = Linha(B, A)

if L1 == L2:
    print("As linhas são iguais")
else:
    print("As linhas NÃO são iguais")

Q = Ponto(10, 10)
if Q == B:
    print("Os pontos são iguais")
else:
    print("Os pontos NÃO são iguais")
