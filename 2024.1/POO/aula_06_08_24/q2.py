class Animal:
    def __init__(self, nome:str, tipo:str, idade:int):
        self.__nome = nome
        self.__tipo = tipo
        self.__idade = idade

    def fazer_aniversario(self):
        self.__idade += 1

    def mostrar_idade(self):
        return self.__idade

gatinho = Animal("Mia", "Gato", 2)

gatinho.fazer_aniversario()
gatinho.fazer_aniversario()

print(gatinho.mostrar_idade())