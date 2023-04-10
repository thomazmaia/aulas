'''
4. Crie um método de classe chamado por_tamanho_e_quadrante(t, q) para que o usuário consiga criar uma ponto com um determinado tamanho em um determinado quadrante.
'''

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


P = Ponto.por_tamanho_e_quadrante(5, 4)
x, y, q = P.get_info()
print(f"Os pontos {x} e {y} estão no quadrante {q}.")