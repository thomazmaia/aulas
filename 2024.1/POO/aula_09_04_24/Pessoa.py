class Pessoa:
    def __init__(self, nome : str, idade : int) -> None:
        self.set_nome(nome)
        self.set_idade(idade)

    def get_nome(self):
        return f"O nome é {self.__nome}"
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self, nome : str):
        if len(nome) < 3:
            print("Nome inválido")
        else:
          self.__nome = nome.capitalize()
    
    def set_idade(self, idade : int):
        self.__idade = idade

p1 = Pessoa("Thomas", 36)
p2 = Pessoa("Yasmim", 17)

print(p1.get_nome())