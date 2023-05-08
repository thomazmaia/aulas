import datetime


class Carro:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = datetime.datetime.now().year

    def get_info(self):
        print(self.marca, self.modelo, self.ano)


class Honda(Carro):
    def __init__(self, modelo) -> None:
        self.marca = "Honda"
        super().__init__(self.marca, modelo)


class Fit(Honda):
    def __init__(self) -> None:
        self.modelo = self.__class__.__name__
        super().__init__(self.modelo)


class HRV(Honda):
    def __init__(self) -> None:
        self.modelo = self.__class__.__name__
        super().__init__(self.modelo)


carro1 = Fit()
carro2 = HRV()

carro1.get_info()
carro2.get_info()
