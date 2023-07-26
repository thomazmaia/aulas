import Geometria as gmt

P1 = gmt.Ponto(6, 3)
P2 = gmt.Ponto(6, 0)
P3 = gmt(2, 0)

tri = gmt.Triangulo(P1, P2, P3)
print(tri.calc_perimetro())