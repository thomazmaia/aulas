class Veiculo:
    def __init__(self, vm) -> None:
        self.velocidade_maxima = vm
        self.velocidade_atual = 0

    def acelerar(self, valor):
        self.velocidade_atual += valor


class Carro(Veiculo):
    def __init__(self, vm, marca) -> None:
        super().__init__(vm)
        self.marca = marca

    def acelerar(self, valor):
        if valor + self.velocidade_atual > self.velocidade_maxima:
            super().acelerar(self.velocidade_maxima - self.velocidade_atual)
            print("Velocidade máxima atingida")
        else:
            super().acelerar(valor)


class Moto(Veiculo):
    def __init__(self, vm, cil) -> None:
        super().__init__(vm)
        self.cilindradas = cil

    def acelerar(self, valor):
        if valor + self.velocidade_atual > self.velocidade_maxima:
            super().acelerar(self.velocidade_maxima - self.velocidade_atual)
            print("Velocidade máxima atingida")
        else:
            super().acelerar(valor)


uno = Carro(vm=180, marca="Fiat")
cg = Moto(vm=120, cil=150)

print(cg.velocidade_atual, "km/h")
cg.acelerar(10)
print(cg.velocidade_atual, "km/h")
cg.acelerar(500)
print(cg.velocidade_atual, "km/h")
