class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def mostrar_detalhes(self):
        print(20*"-")
        print(f"Nome: {self.nome} - {self.idade} anos")
        print(f"CPF: {self.cpf}")
        print(20*"-")

    def fazer_aniversario(self):
        self.idade += 1


nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
cpf = int(input("Digite o CPF da pessoa: "))

aluno = Pessoa(nome, idade, cpf)
aluno.fazer_aniversario()
aluno.fazer_aniversario()
aluno.fazer_aniversario()
print(idade)
print(aluno.idade)
