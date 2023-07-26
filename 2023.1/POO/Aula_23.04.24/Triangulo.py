from Ponto import *

class Triangulo:
    def __init__(self, p1, p2, p3) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @staticmethod
    def get_lados(p1, p2, p3):
        L1 = Ponto.calc_dist_entre_pontos(p1, p2)
        L2 = Ponto.calc_dist_entre_pontos(p2, p3)
        L3 = Ponto.calc_dist_entre_pontos(p3, p1)
        return (L1, L2, L3)


    @staticmethod
    def calc_lado(A, B):
        return Ponto.calc_dist_entre_pontos(A, B)
    
    def calc_perimetro(self):
        A = Ponto.calc_dist_entre_pontos(self.p1, self.p2)
        B = Ponto.calc_dist_entre_pontos(self.p2, self.p3)
        C = Ponto.calc_dist_entre_pontos(self.p3, self.p1)
        return A + B + C    

    def verifica(self):
        (L1, L2, L3) = self.get_lados(self.p1, self.p2, self.p3)
        if L1 == L2 and L2 == L3:
            print("Triângulo equilátero")
        elif L1 != L2 and L2 != L3 and L3 != L1:
            print("Triângulo escaleno")
        else:
            print("Triângulo isóceles")

    def calc_area(self):
        L1, L2, L3 = self.get_lados(self.p1, self.p2, self.p3)
        p = (L1 + L2 + L3)/2
        a = math.sqrt(p * (p - L1) * (p - L2) * (p - L3))
        return a


p1 = Ponto(0, 0)
p2 = Ponto(4, 0)
p3 = Ponto(4, 3)

tri = Triangulo(p1, p2, p3)
tri.verifica()
tri.calc_area()
