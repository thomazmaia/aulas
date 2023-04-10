''' 1. Crie uma classe chamada Ponto. Essa classe deve receber dois valores X, Y (float) no seu construtor. Faça os getters e setters para esses atributos serem chamados pelo main abaixo:
P = Ponto(50,50) print(f"Coordenadas: {P.x},{P.y}")
P.x = 20
print(f"Novas coordenadas: {P.x},{P.y}")
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

P = Ponto(50, 50)
print(f"Coordenadas: ({P.x},{P.y})")
P.x = 20
print(f"Coordenadas: ({P.x},{P.y})")