class Veiculo:
    def locomoverSe(self, local):
        print(f"Estou me locomovendo {local}")


class Carro(Veiculo):
    def locomoverSe(self):
        super().locomoverSe("no asfalto")


class Barco(Veiculo):
    def locomoverSe(self):
        super().locomoverSe("na água")


class Aviao(Veiculo):
    def locomoverSe(self):
        super().locomoverSe("no ar")


class Elevador(Veiculo):
    def locomoverSe(self):
        super().locomoverSe("no prédio")


carro = Carro()
carro.locomoverSe()

barco = Barco()
barco.locomoverSe()

aviao = Aviao()
aviao.locomoverSe()

elevador = Elevador()
elevador.locomoverSe()
