from math import sqrt

class Ponto:
    def __init__(self, x:float, y:float):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x:float):
        self.__x = x

    def set_y(self, y:float):
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
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
    

P1 = Ponto(10, -20)
P2 = Ponto.por_tamanho_e_quadrante(5, 3)
print(P2.get_x(), P2.get_y())