from abc import ABC, abstractmethod
import math


class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Retangulo(FiguraGeometrica):
    def __init__(self, b, h) -> None:
        self.base = b
        self.altura = h

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(FiguraGeometrica):
    def __init__(self, r) -> None:
        self.raio = r

    def calcular_area(self):
        return math.pi * self.raio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio


R = Retangulo(10, 10)
print(R.calcular_area())

C = Circulo(10)
print(C.calcular_area())
