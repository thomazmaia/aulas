class Pessoa:
    def __init__(self, nome, animal) -> None:
        self.nome = nome
        self.animal = animal

class Pet:
    def __init__(self, nome, raca) -> None:
        self.nome = nome
        self.raca = raca

animal = Pet("Totó", "Pitbul")
pessoa = Pessoa("João", animal)

print(f"{pessoa.nome} tem um {pessoa.animal.raca} de nome {pessoa.animal.nome}")

del pessoa

print(f"{animal.nome}")