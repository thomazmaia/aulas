class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, novo_x):
        self._x = novo_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, novo_y):
        self._y = novo_y

P = Ponto(3, 4)
print(P.x, P.y)
P.x = 0
P.y = 0
print(P.x, P.y)