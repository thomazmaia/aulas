class Animal:
    def __init__(self, nome, idade, especie, som) -> None:
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.som = som

    def fazer_som(self):
        print(self.som)

    def envelhecer(self, anos):
        self.idade += anos


class Cachorro(Animal):
    def __init__(self, nome, idade, especie, raca, latido) -> None:
        super().__init__(nome, idade, especie, latido)
        self.__raca = raca
        self.__latido = latido

    def latir(self):
        super().fazer_som()

    def set_raca(self, nova_raca):
        self.__raca = nova_raca


dog = Cachorro("Rex", 1, "Hominus-cachorrus", "Vira-lata", "Au au au")
dog.latir()
