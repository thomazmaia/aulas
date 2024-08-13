from math import sqrt

class Ponto:
    def __init__(self, x:float, y:float):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x:float):
        self.__x = x

    def set_y(self, y:float):
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_info(self):
        return (self.get_x(), self.get_y())

    @classmethod
    def por_tamanho_e_quadrante(cls, t:float, q:int):
        c = sqrt(t*t/2)
        if q == 1: # x e y positivos
            x = c
            y = x
        elif q == 2: # y positivo e x negativo
            x = -c
            y = c
        elif q == 3: # x e y negativos
            x = -c
            y = -c
        elif q == 4: # x positivo e y negativo
            x = c
            y = -c
        p = cls(x, y)
        return p
    
    @staticmethod
    def calc_dist_entre_pontos(a, b):
        dist = sqrt( (a.get_x() - b.get_x())**2 + (a.get_y() - b.get_y())**2 )
        return dist

    

class Triangulo:
    def __init__(self, p1:Ponto, p2:Ponto, p3:Ponto):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
    
    def calc_perimetro(self):
        L1 = Ponto.calc_dist_entre_pontos(self.__p1, self.__p2)
        L2 = Ponto.calc_dist_entre_pontos(self.__p2, self.__p3)
        L3 = Ponto.calc_dist_entre_pontos(self.__p3, self.__p1)
        perimetro = (L1 + L2 + L3)
        return perimetro


