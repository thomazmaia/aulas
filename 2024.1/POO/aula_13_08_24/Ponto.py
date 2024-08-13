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