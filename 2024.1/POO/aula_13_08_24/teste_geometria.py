from Geometria import Ponto, Triangulo

P1 = Ponto(0, 0)
P2 = Ponto(20, 0)
P3 = Ponto(0, 10)

T = Triangulo(P1, P2, P3)
print(T.calc_perimetro())
