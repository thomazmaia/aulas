class Barco:
    def navegar(self):
        print("Navegando...")

class Carro:
    def mover(self):
        print("Movendo...")

class VeiculoAnfibio(Barco, Carro):
    pass

X = VeiculoAnfibio()
X.mover()
X.navegar()