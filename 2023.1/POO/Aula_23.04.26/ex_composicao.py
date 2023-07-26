class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        meu_endereco = Endereco(cidade, estado)
        self.enderecos.append(meu_endereco)

    def listar_enderecos(self):
        print(f"Listando endereços do cliente: {self.nome}")
        for item in self.enderecos:
            print(f"{self.nome} mora em {item.cidade}/{item.estado}")


class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado



c1 = Cliente("João", 20)
c2 = Cliente("Maria", 30)

c1.inserir_endereco("Maranguape", "CE")
c1.inserir_endereco("Fortaleza", "CE")
c1.inserir_endereco("Maracanau", "CE")

del c1

print(c1.enderecos[0].cidade)