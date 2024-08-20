class Endereco:
    def __init__(self, cidade:str, estado:str) -> None:
        self.cidade = cidade
        self.estado = estado


class Cliente:
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = list()

    def insere_endereco(self, cidade:str, estado:str):
        meu_endereco = Endereco(cidade, estado)
        self.enderecos.append(meu_endereco)

    def listar_enderecos(self):
        for end in self.enderecos:
            print(end.cidade, end.estado)


C = Cliente("Thomaz", 36)
C.insere_endereco("Eusébio", "CE")
C.insere_endereco("Maranguape", "CE")
C.listar_enderecos()

D = Cliente("Maria", 20)
D.insere_endereco("Eusébio", "CE")

del C

C.listar_enderecos()