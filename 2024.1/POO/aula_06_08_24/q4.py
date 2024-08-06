import math

class Triangulo:
    def __init__(self, l3:float, l2:float, l1:float):
        self.__lado1 = l1
        self.__lado2 = l2
        self.__lado3 = l3

    def calc_perimetro(self):
        p = (self.__lado1 + self.__lado2 + self.__lado3)/2
        return p

    def calc_area(self):
        p = self.calc_perimetro()
        a = self.__lado1
        b = self.__lado2
        c = self.__lado3
        a = math.sqrt(p*(p - a)*(p - b)*(p - c))
        return a


T = Triangulo(26, 26, 20)

perimetro = T.calc_perimetro()
print(f"O perímetro é de {perimetro}")

area = T.calc_area()
print(f"A área é de {area}")