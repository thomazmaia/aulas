class Pet:
    def __init__(self, nome:str, raca:str) -> None:
        self.nome = nome
        self.raca = raca

class Pessoa:
    def __init__(self, nome:str, animal:Pet):
        self.nome = nome
        self.animal_de_estimacao = animal


pet1 = Pet("Auau", "Vira-lata")

pessoa1 = Pessoa("Fulano", pet1)
print("")