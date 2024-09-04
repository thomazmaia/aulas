class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self, alt:int, larg:int):
        super().__init__()
        self.altura = alt
        self.largura = larg

    def calcular_area(self):
        self.area = self.altura * self.largura
        return self.area

    def calcular_perimetro(self):
        self.perimetro = 2 * (self.altura + self.largura)
        return self.perimetro

class Triangulo(Forma):
    def __init__(self, base:int, altura:int):
        super().__init__()
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        self.area = (self.base * self.altura)/2
        return self.area

    def calcular_perimetro(self):
        self.perimetro = 3 * self.base
        return self.perimetro

T = Triangulo(6, 4)
R = Retangulo(5, 3)


print(f"Área e perímetro do triângulo: {T.calcular_area()} e {T.calcular_perimetro()}")
print(f"Área e perímetro do retângulo: {R.calcular_area()} e {R.calcular_perimetro()}")


print(isinstance(T, Forma))
print(isinstance(R, Forma))