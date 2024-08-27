class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass

class Vendedor(Pessoa):
    pass


P = Pessoa("xico", 10)
C = Cliente("Ze", 20)