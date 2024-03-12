#Classe Pessoa
#• Atributos: nome (str), idade (int), CPF (int)
#• Métodos: mostrar_detalhes(), fazer_aniversário()

class Pessoa:
    def __init__(self, nome : str, idade : int, cpf : int) -> None:
        self.nome = nome
        self.idade = idade
        self.CPF = cpf

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Idade = {self.idade} | CPF = {self.CPF}")

    def fazer_aniversario(self):
        self.idade += 1



yasmim = Pessoa("Yasmim", 17, 12345678900)
yasmim.mostrar_detalhes()

jv = Pessoa("João Victor", 17, 1111111100)
jv.mostrar_detalhes()
jv.fazer_aniversario()
jv.mostrar_detalhes()