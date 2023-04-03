class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método de instância
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
    # Método de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        id = cls.ano_atual - ano_nascimento
        return cls(nome, id)

    # Método estático
    @staticmethod
    def gera_cartao_de_visita(nome, idade):
        print("-------------------------------------------")
        print(f"Olá, me chamo {nome} e tenho {idade} anos.")
        print("-------------------------------------------")
    


luan = Pessoa("Luan", 18)
print(luan.get_ano_nascimento())

lana = Pessoa("Lana", 16)
print(lana.get_ano_nascimento())

andre = Pessoa.por_ano_nascimento("Andre", 2006)
print(andre.get_ano_nascimento())

Pessoa.gera_cartao_de_visita("Emilly", 17)
luan.gera_cartao_de_visita("ÊMELE", 17)