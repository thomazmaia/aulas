class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0

    def set_nome(self, N : str):
        self.__nome = N

    def set_idade(self, id: int):
        self.__idade = id

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade

P = Pessoa()
P.__nome = "Xico"  # NÃO FUNCIONA. NÃO MUDA O ATRIBUTO DA CLASSE
P.__idade = 10     # NÃO FUNCIONA. NÃO MUDA O ATRIBUTO DA CLASSE

print(P.get_nome(), P.get_idade())

P.set_nome("João Paulo")
P.set_idade(17)

print(P.get_nome(), P.get_idade())

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
P.set_nome(nome)
P.set_idade(idade)

print(P.get_nome(), P.get_idade())