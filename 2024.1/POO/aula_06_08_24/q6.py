class ContaCorrente:
    def __init__(self, numero:int, saldo:float, titular:str, limite:float):
        self.__numero_conta = numero
        self.__saldo = saldo
        self.__titular = titular
        self.__limite_saque = limite

    def depositar(self, valor:float):
        self.__saldo += valor

    def sacar(self, valor:float):
        if valor > self.__limite_saque:
            print("[LIMITE DE SAQUE ATINGIDO]")
        elif valor > self.__saldo:
            print("[SALDO INSUFICIENTE]")
        else:
            self.__saldo -= valor  

    def consultar_saldo(self):
        print("Consultando saldo...")
        print(f"Salto atual: R$ {self.__saldo}")


CC = ContaCorrente(123456, 1000, "Joáo da Silva", 500)
CC.depositar(500)
CC.sacar(300)
CC.sacar(600)

CC.consultar_saldo()