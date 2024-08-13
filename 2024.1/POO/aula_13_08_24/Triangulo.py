import Ponto as pt

class Triangulo:
    def __init__(self, p1:pt.Ponto, p2:pt.Ponto, p3:pt.Ponto):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
    
    def calc_perimetro(self):
        L1 = self.calc_lado(self.__p1, self.__p2)
        L2 = self.calc_lado(self.__p2, self.__p3)
        L3 = self.calc_lado(self.__p3, self.__p1)
        perimetro = (L1 + L2 + L3)
        return perimetro
    
    def calc_lado(self, A:pt.Ponto, B:pt.Ponto):
        return pt.Ponto.calc_dist_entre_pontos(A, B)
    
    def calc_area(self):
        p = self.calc_perimetro()/2
        L1 = self.calc_lado(self.__p1, self.__p2)
        L2 = self.calc_lado(self.__p2, self.__p3)
        L3 = self.calc_lado(self.__p3, self.__p1)
        area = pt.sqrt(p*(p - L1)*(p - L2)*(p - L3))
        return area  

    def verifica(self):
        L1 = self.calc_lado(self.__p1, self.__p2)
        L2 = self.calc_lado(self.__p2, self.__p3)
        L3 = self.calc_lado(self.__p3, self.__p1)    
        if L1 == L2 and L2 == L3:
            return "Equilátero"    
        elif L1 != L2 and L2 != L3 and L3 != L1:
            return "Escaleno"
        else:
            # Ta errado mas vai ficar
            return "Isóceles"


P1 = pt.Ponto(6, 7)
P2 = pt.Ponto(8, 2)
P3 = pt.Ponto(4, 2)

T = Triangulo(P1, P2, P3)
print(T.calc_perimetro())
print(T.calc_lado(P1, P2))
print(T.calc_lado(P2, P3))
print(T.calc_lado(P3, P1))
print(T.calc_area())
print(T.verifica())