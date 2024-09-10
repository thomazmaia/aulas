class Animal:
    def __init__(self, nome:str) -> None:
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo")


class Cachorro(Animal):
    def latir(self):
        print("Au au")


class Gato(Animal):
    def miar(self):
        print("Miau")

toto = Cachorro("Totó")
mel = Gato("Mel")

lista_de_animais = [toto, mel]

for animal in lista_de_animais:
    animal.comer()