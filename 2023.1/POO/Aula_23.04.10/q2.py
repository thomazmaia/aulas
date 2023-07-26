'''
2. Adicione um método de instância à classe Ponto chamado get_info(). Esse método deve retornar as coordenadas e o quadrante daquele ponto.
'''
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

P = Ponto(50, 50)
x, y, q = P.get_info()
print(f"Os pontos {x} e {y} estão no quadrante {q}.")

P.x = -35
x, y, q = P.get_info()
print(f"Os pontos {x} e {y} estão no quadrante {q}.")