class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, endereco):
        meu_endereco = endereco
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

meu_endereco1 = Endereco("Maranguape", "CE")
meu_endereco2 = Endereco("Fortaleza", "CE")
meu_endereco3 = Endereco("Maracanau", "CE")

c1.inserir_endereco(meu_endereco1)
c1.inserir_endereco(meu_endereco2)
c1.inserir_endereco(meu_endereco3)

del meu_endereco1

print(c1.enderecos[0].cidade)
print(meu_endereco1.cidade)