class Barco:
    def __init__(self) -> None:
        self.eu = self.__class__.__name__

    def navegar(self):
        print(f"{self.eu} está navegando")


class Carro:
    def __init__(self) -> None:
        self.eu = self.__class__.__name__

    def andar(self):
        print(f"{self.eu} está andando")


class VeiculoAnfibio(Barco, Carro):
    pass


carrco = VeiculoAnfibio()
carrco.andar()
carrco.navegar()
