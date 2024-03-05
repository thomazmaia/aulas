class Fila:
    def __init__(self):
        self.quantidade_de_pessoas = 0

    def aumentar(self):
        self.quantidade_de_pessoas += 1

    def diminuir(self):
        self.quantidade_de_pessoas -= 1



F = Fila()
F.aumentar()
F.aumentar()
F.aumentar()
F.aumentar()
F.aumentar()
F.diminuir()
F.diminuir()

print(F.quantidade_de_pessoas)