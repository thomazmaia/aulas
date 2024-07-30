# Crie uma classe chamada Retangulo com os atributos base e altura. Crie métodos para calcular a área e o perímetro do retângulo. Crie um objeto da classe Retangulo com os seguintes valores para os atributos:
# - base: 10
# - altura: 5
# Calcule e imprima a área e o perímetro do retângulo utilizando os métodos criados.

class Retangulo:
    def __init__(self, base:float, altura:float) -> None:
        self.__base = base
        self.__altura = altura

    def calc_area(self):
        return self.__base * self.__altura

    def calc_perimetro(self):
        return (2 * (self.__base + self.__altura))
    

R = Retangulo(10, 5)
print(f"Área: {R.calc_area()}")
print(f"Perímetro: {R.calc_perimetro()}")