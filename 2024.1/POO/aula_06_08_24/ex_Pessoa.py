class Pessoa:
    ano = 2024

    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade

    # Método de instância
    def get_ano_nascimento(self):
        print(f"Nasceu em {self.ano - self.__idade}")
    
    # Método de classe
    @classmethod
    def por_ano_nascimento(cls, nome:str, ano_nascimento:int):
        idade = cls.ano - ano_nascimento
        return cls(nome, idade)
    
    # Método estático
    @staticmethod
    def gera_cartao_de_visita(nome:str, idade:int):
        print(f"{nome} - {idade} anos")


yasmin = Pessoa("Yasmin", 17)
yasmin.get_ano_nascimento()

jp = Pessoa.por_ano_nascimento("João Paulo", 2005)
jp.get_ano_nascimento()

Pessoa.gera_cartao_de_visita("Lara", 17)