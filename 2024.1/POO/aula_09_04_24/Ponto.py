class Ponto:
    def __init__(self, x : float, y : float) -> None:
        self.set_X(x)
        self.set_Y(y)

    def set_X(self, x):
        self.__X = x

    def set_Y(self, y):
        self.__Y = y

    def get_X(self):
        return self.__X
    
    def get_Y(self):
        return self.__Y

P = Ponto(50, 50)
print(f"Coordenadas: {P.get_X()},{P.get_Y()}")

P.set_Y(20)
print(f"Coordenadas: {P.get_X()},{P.get_Y()}")