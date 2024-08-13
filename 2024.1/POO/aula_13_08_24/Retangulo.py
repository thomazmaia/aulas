import Ponto as pt

class Retangulo:
    def __init__(self, p1:pt.Ponto, p2:pt.Ponto, p3:pt.Ponto, p4:pt.Ponto) -> None:
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__p4 = p4
    
    def calc_perimetro(self):
        L1 = pt.Ponto.calc_dist_entre_pontos(self.__p1, self.__p2)
        L2 = pt.Ponto.calc_dist_entre_pontos(self.__p2, self.__p3)
        perimetro = 2*(L1 + L2)
        return perimetro
    
    def calc_area(self):
        L1 = pt.Ponto.calc_dist_entre_pontos(self.__p1, self.__p2)
        L2 = pt.Ponto.calc_dist_entre_pontos(self.__p2, self.__p3)        
        area = L1 * L2
        return area
    

P1 = pt.Ponto(0,0)
P2 = pt.Ponto(50,0)
P3 = pt.Ponto(50,20)
P4 = pt.Ponto(0,20)

R = Retangulo(P1, P2, P3, P4)
print(R.calc_perimetro())
print(R.calc_area())