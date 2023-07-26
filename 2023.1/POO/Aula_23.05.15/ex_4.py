class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Oi, meu nome é {self.nome} e eu tenho {self.idade} anos.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, data_admissao) -> None:
        super().__init__(nome, idade)
        self.salario = salario
        self.data_admissao = data_admissao

    def calcular_bonus(self):
        return self.salario * 0.1


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, data_admissao, setor) -> None:
        super().__init__(nome, idade, salario, data_admissao)
        self.setor = setor

    def calcular_bonus(self):
        return self.salario * 0.5


Pedro = Gerente("Pedro", 40, 5000, "março", "Vendas")
print(Pedro.calcular_bonus())

Paulo = Funcionario("Paulo", 40, 5000, "março")
print(Paulo.calcular_bonus())
