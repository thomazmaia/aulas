# 3. Crie uma classe chamada Pessoa com os atributos nome e idade. Crie um método chamado fazer_aniversario que incrementa a idade da pessoa em 1 ano. Crie um objeto da classe Pessoa chamado joao com os seguintes valores para os atributos:
# - nome: João
# - idade: 25
# Chame o método fazer_aniversario duas vezes para o objeto joao e imprima a idade atual de joao após cada chamada do método.

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade

    def fazer_aniversario(self):
        self.__idade += 1

    def get_idade(self):
        return self.__idade

joao = Pessoa("João", 25)

joao.fazer_aniversario()
joao.fazer_aniversario()

print(joao.get_idade())