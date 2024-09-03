import datetime

class Pessoa:
    def __init__(self, nome:str, cpf:int) -> None:
        self.nome = nome
        self.cpf = cpf

class LogMixin:
    @staticmethod
    def write(msg):
        with open("log.txt", "a+") as f:
            f.write(msg)
            f.write("\n")
    
    def log_msg(self, msg):
        self.write(f"[LOG] {msg}")



class Funcionario(Pessoa, LogMixin):
    def __init__(self, nome: str, cpf: int):
        self.cargo = "Estagiário"
        self.salario = 500
        super().__init__(nome, cpf)
        self.log_msg(f"{self.nome} contratado como {self.cargo}")

    def promover(self):
        if self.cargo == "Estagiário":
            self.cargo = "Vendedor"
            self.salario += 200
        elif self.cargo == "Vendedor":
            self.cargo = "Supervisor"
            self.salario += 300
        elif self.cargo == "Supervisor":
            self.cargo = "Gerente Geral"
            self.salario += 500
        print(f"{self.nome} foi promovido a {self.cargo}")
        self.log_msg(f"{self.nome} foi promovido a {self.cargo}")

    def demitir(self):
        print(f"{self.nome} foi demitido.")
        self.log_msg(f"{self.nome} foi demitido.")
    
    def cortar_ponto(self):
        val_dia = self.salario/30
        self.salario -= val_dia
        self.log_msg(f"{self.nome} teve o ponto cortado.")



Ze = Funcionario("Jose", 123)

Ze.promover()
Ze.promover()
Ze.cortar_ponto()
Ze.cortar_ponto()
Ze.cortar_ponto()
Ze.cortar_ponto()