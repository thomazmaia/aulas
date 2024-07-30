# 6. Crie uma classe chamada ContaBancaria com os atributos numero_conta, saldo e titular. Crie métodos para depositar e sacar valores da conta. Implemente o método sacar para que ele só permita sacar valores que não excedam o saldo da conta. Crie um objeto da classe ContaBancaria com os seguintes valores para os atributos:
# - numero_conta: 123456
# - saldo: 1000
# - titular: João da Silva
# Realize as seguintes operações e imprima o saldo após cada operação:

# Depositar R$500.
# Sacar R$300.
# Sacar R$800 (o método sacar deve impedir a operação e imprimir uma mensagem de erro).
# Dica: Utilize o conceito de getters e setters para controlar o acesso e a modificação do atributo saldo da classe ContaBancaria.

class ContaBancaria:
    def __init__(self, num:int, saldo:float, titular:str):
        self.__numero_da_conta = num
        self.__saldo = saldo
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor:float):
        self.__saldo += valor

    def sacar(self, valor:float):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("[ERRO] Saldo insuficiente")
    

conta = ContaBancaria(123456, 1000, "João da Silva")

conta.depositar(500)
conta.sacar(300)
conta.sacar(1800)

print(f"Saldo disponível: R${conta.get_saldo()}")