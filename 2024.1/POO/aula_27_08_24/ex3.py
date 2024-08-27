from datetime import datetime

class Carro:
    def __init__(self, marca:str, modelo:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = datetime.now().year

    def get_info(self):
        print(f"{self.marca} {self.modelo} ano {self.ano}")


class Toyota(Carro):
    def __init__(self, modelo:str):
        self.marca = "Toyota"
        super().__init__(self.marca, modelo)

class Corolla(Toyota):
    def __init__(self):
        self.modelo = "Corolla"
        super().__init__(self.modelo)

class Etios(Toyota):
    def __init__(self):
        self.modelo = "Etios"
        super().__init__(self.modelo)


carro = Corolla()
carro.get_info()

carro2 = Etios()
carro2.get_info()

C = Carro("Toyota", "Hilux")
C.get_info()