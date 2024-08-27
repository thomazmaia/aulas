class Pessoa:
    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf
        self.nome_classe = self.__class__.__name__

    def mostra_cpf(self):
        print(self.cpf)

class Aluno(Pessoa):
    def em_aula(self):
        print(f"{self.nome_classe} está em aula")
    

class Professor(Pessoa):
    def em_aula(self):
        print(f"{self.nome_classe} está em aula")

class AlunoTecnico(Aluno):
    def __init__(self, nome:str, curso:str, cpf:str):
        self.curso_tecnico = curso       
        super().__init__(nome, cpf) 

    def em_aula(self):
        print(f"{self.nome_classe} está em aula")

    def mostra_cpf(self):
        self.cpf = "xxx"
        return super().mostra_cpf()


A = Aluno("Yasmim", "123")
P = Professor("Thomaz", "456")
AT = AlunoTecnico("João Victor", "Informática", "111")

A.mostra_cpf()
P.mostra_cpf()
AT.mostra_cpf()