# Crie uma classe chamada Carro com os atributos marca, modelo e ano. Crie um método chamado mostrar_dados que imprime os valores dos atributos do objeto. Crie um objeto da classe Carro chamado fusca com os seguintes valores para os atributos:
# - marca: Volkswagen
# - modelo: Fusca
# - ano: 1970
# Chame o método mostrar_dados para o objeto fusca.

class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    
    def mostrar_dados(self):
        print(f"{self.__marca} {self.__modelo} ano {self.__ano}")


fusca = Carro("VolksWagen", "Fusca", 1970)
fusca.mostrar_dados()