# Crie uma classe chamada Veiculo que possua um atributo velocidade_maxima e um método acelerar(), que incrementa um valor passado como parâmetro à "velocidade_atual" do veículo. Em seguida, crie duas subclasses chamadas Carro e Moto, que  herdam da classe Veiculo. A classe Carro deve ter um atributo adicional "marca" e a classe Moto deve ter um atributo adicional "cilindradas". Cada subclasse deve sobrescrever o método acelerar() para verificar se a velocidade atual não ultrapassou a sua respectiva velocidade máxima. Se ultrapassou, deve imprimir a mensagem “Velocidade máxima atingida”. Caso contrário, deve chamar o método acelerar() da superclasse.

class Veiculo:
    def __init__(self, vm:int):
        self.velocidade_maxima = vm
        self.velocidade_atual = 0

    def acelerar(self, val:int):
        self.velocidade_atual += val


class Carro(Veiculo):
    def __init__(self, marca:str, vm:int):
        self.marca = marca
        super().__init__(vm)

    def acelerar(self, val: int):
        if (val + self.velocidade_atual) <= self.velocidade_maxima:
            return super().acelerar(val)
        else:
            print("Velocidade máxima atingida")


class Moto(Veiculo):
    def __init__(self, cil:int, vm: int):
        self.cilinidradas = cil
        super().__init__(vm)

    def acelerar(self, val: int):
        if (val + self.velocidade_atual) <= self.velocidade_maxima:
            return super().acelerar(val)
        else:
            print("Velocidade máxima atingida")        


carro = Carro('Fiat', 120)  # Marca e velocidade maxima
moto = Moto(250, 100) # Cilindradas e velocidade maxima

carro.acelerar(110)
moto.acelerar(120)

print(carro.velocidade_atual)
print(moto.velocidade_atual)