class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass


class Vendedor(Pessoa):
    pass


P = Pessoa("Thomaz", 35)
print(P.nome)

C = Cliente()
print(C.nome)

A = Aluno()
print(A.nome)

V = Vendedor()
print(V.nome)
