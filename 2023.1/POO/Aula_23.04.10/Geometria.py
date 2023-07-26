import math

class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # GETTER do X
    @property
    def x(self):
        return self._x
    
    # SETTER do X
    @x.setter
    def x(self, x):
        self._x = x

    # GETTER do Y
    @property
    def y(self):
        return self._y
    
    # sETTER do Y
    @y.setter
    def y(self, y):
        self._y = y

    def get_info(self):
        quadrante = ''
        if self.x > 0 and self.y > 0:
            quadrante = 'Quadrante 1'
        elif self.x < 0 and self.y > 0:
            quadrante = 'Quadrante 2'
        elif self.x < 0 and self.y < 0:
            quadrante = 'Quadrante 3'
        elif self.x > 0 and self.y < 0:
            quadrante = 'Quadrante 4'
        return self.x, self.y, quadrante
    
    @classmethod
    def por_tamanho_e_quadrante(cls, t, q):
        hipotenusa = t
        cateto = hipotenusa * 0.705
        x = cateto
        y = cateto
        if q == 2:
            x = -cateto
        elif q == 3:
            x = -cateto
            y = -cateto
        elif q == 4:
            y = -cateto
        return cls(x, y)

    @staticmethod
    def calc_dist_entre_pontos(p1, p2):
        cateto1 = p2.y - p1.y
        cateto2 = p2.x - p1.x
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        return hipotenusa

class Triangulo:
    def __init__(self, p1, p2, p3) -> None:
        self.P1 = p1
        self.P2 = p2
        self.P3 = p3

    def calc_perimetro(self):
        A = Ponto.calc_dist_entre_pontos(self.P1, self.P2)
        B = Ponto.calc_dist_entre_pontos(self.P2, self.P3)
        C = Ponto.calc_dist_entre_pontos(self.P3, self.P1)
        return A + B + C
