class Conta:
    def __init__(self, ag, num, lim=1000) -> None:
        self.agencia = ag
        self.numero = num
        self.limite = lim
        self.historico = []
        self.saldo = 0

    def verifica_saldo(self):
        return self.saldo

    def extrato(self):
        print("-----------")
        print("- EXTRATO -")
        print("-----------")
        for item in self.historico:
            print(item)

    def saque(self, valor):
        if valor >= self.saldo + self.limite:
            print("Sem grana, irmão.")
        else:
            self.saldo -= valor
            self.historico.append(f"[SAQUE] R$ {valor}  - [SALDO] R$ {self.saldo}")

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f"[DEPÓSITO] R$ {valor}  - [SALDO] R$ {self.saldo}")

    def transferir(self, outra_conta, valor):
        pass


c1 = Conta("1234", "888-9", 50)
c2 = Conta("1234", "888-9", 50)

c1.transferir(c2, 500)

c1.deposito(-300)
c1.saque(130)
c1.deposito(132)
c1.deposito(362)
c1.deposito(752)
c1.saque(1000)
c1.saque(500)
c1.extrato()