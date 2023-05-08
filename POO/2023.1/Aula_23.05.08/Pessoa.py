class Pessoa:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.CPF = cpf
        self.nome_classe = self.__class__.__name__

    def mostra_cpf(self):
        print(self.CPF)


class Professor(Pessoa):
    def em_aula(self):
        return f"{self.nome_classe} Está em aula..."


class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula) -> None:
        self.matricula = matricula
        super().__init__(nome, cpf)

    def em_aula(self):
        return f"{self.nome_classe} Está em aula..."


class AlunoTecnico(Aluno):
    def __init__(self, nome_da_pessoa, cpf_da_pessoa, nome_curso, matricula):
        self.curso_tecnico = nome_curso
        super().__init__(nome_da_pessoa, cpf_da_pessoa, matricula)


ze = Professor("José", 000)
xico = Aluno("Francisco", 123, 444)
mama = AlunoTecnico("Maria", 555, "Informática", 123)

mama.mostra_cpf()
