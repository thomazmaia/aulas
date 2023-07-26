class Pessoa:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf


class LogMixIn:
    @staticmethod
    def write(msg):
        with open("log.txt", "a") as f:
            f.write(msg)
            f.write("\n")

    def log_msg(self, msg):
        self.write(f"LOG: {msg}")


class Funcionario(Pessoa, LogMixIn):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.cargo = "Estagiário"
        self.salario = 500
        self.log_msg(f"{self._nome} contratado como estagiário")

    def promover(self, cargo, aumento):
        self.log_msg(f"{self._nome} promovido de {self.cargo} para {cargo}.")
        self.cargo = cargo
        self.salario += aumento

    def demitir(self):
        self.log_msg(f"{self._nome} foi demitido.")
        del self

    def cortar_ponto(self, dias):
        self.log_msg(f"Cortando o ponto de {self._nome} por {dias} dias.")
        self.salario -= dias * 10


Joao = Funcionario("Joao", 123)
Xico = Funcionario("Francisco", 321)

Joao.promover("Supervisor", 300)
Xico.cortar_ponto(5)
Xico.cortar_ponto(5)
Joao.demitir()
Xico.promover("Supervisor", 500)
