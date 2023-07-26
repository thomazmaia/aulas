class Pessoa:
    # Construtor
    def __init__(self, nome, data, cpf):
        # Atributos de classe
        self.nome = nome
        self.data_de_nascimento = data
        self.cpf = cpf

    def calcular_idade(self):
        ano_da_pessoa = int(self.data_de_nascimento[6:11])
        res = 2023 - ano_da_pessoa
        print(f"O {self.nome} tem {res} anos (ou vai fazer esse ano).")

    def exibir_informacoes(self):
        print(60*"-")
        print(f"Nome: {self.nome} - CPF: {self.cpf} - Data de nascimento: {self.data_de_nascimento}")
        print(60*"-")


class Agenda:
    def __init__(self):
        # Atributos de classe
        self.limite = 10
        self.lista = []

    def armazenar_pessoa(self, nome, nascimento, cpf):
        if len(self.lista) == 10:
            print("Agenda cheia!")
        else:
            P = Pessoa(nome, nascimento, cpf)
            self.lista.append(P)

    def remover_pessoa(self, nome):
        for pessoa in self.lista:
            if nome == pessoa.nome:
                self.lista.remove(pessoa)

    def buscar_pessoa(self, nome): 
        # informa em que posição da agenda está a pessoa
        for index, item in enumerate(self.lista):
            if nome == item.nome:
                print(f"O {nome} está na posição {index+1} da agenda.")

    def imprimir_agenda(self):
        # mostra os dados de todas as pessoas na agenda
        print("-------- Agenda: -------- ")
        for index, item in enumerate(self.lista):
            print(f"{index+1}: {item.nome}")
        print("------------------------- ")

    def imprimir_pessoa(self, index):
        # mostra os dados da pessoa na posição ‘index’ da agenda
        self.lista[index-1].exibir_informacoes()