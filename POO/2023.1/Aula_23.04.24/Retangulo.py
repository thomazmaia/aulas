from Ponto import *
from Triangulo import *

class Retangulo:
    def __init__(self, p1, p2, p3, p4) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.ordena_pontos()

    def ordena_pontos(self):
        pass

    def calc_perimetro(self):
        A = Ponto.calc_dist_entre_pontos(self.p1, self.p2)
        B = Ponto.calc_dist_entre_pontos(self.p2, self.p3)
        C = Ponto.calc_dist_entre_pontos(self.p3, self.p4)
        D = Ponto.calc_dist_entre_pontos(self.p4, self.p1)
        return A + B + C + D

    def calc_area(self):
        tri = Triangulo(self.p1, self.p2, self.p3)
        area_tri = tri.calc_area()
        area_ret = 2*area_tri
        return area_ret        


p1 = Ponto(0, 30)
p2 = Ponto(40, 30)
p3 = Ponto(40, 0)
p4 = Ponto(0, 0)

ret = Retangulo(p1, p2, p3, p4)
print(f"Perimetro = {ret.calc_perimetro()}")
print(f"Area = {ret.calc_area()}")