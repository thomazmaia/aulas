# Crie uma classe mãe (base) chamada Veiculo com os atributos marca, modelo e ano. Essa classe deve possuir os métodos ligar ("ligando veículo") e desligar ("desligando veículo"). Crie uma classe filha chamada Carro que herda de Veiculo e sobrescreve o seu construtor. A classe Carro possui, além de marca, modelo e ano, um atributo chamado número_de_portas. Crie um método abrir_portas ("abrindo portas") para a classe Carro.
# Ao final, teste as classes.

class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print("Ligando veículo...")

    def desligar(self):
        print("Desligando veículo...")


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, num:int):
        super().__init__(marca, modelo, ano)
        self.numero_de_portas = num

    def abrir_portas(self):
        print("Abrindo portas...")


meu_carro = Carro("Toyota", "Corolla", 2024, 4)
meu_carro.ligar()
meu_carro.desligar()
meu_carro.abrir_portas()