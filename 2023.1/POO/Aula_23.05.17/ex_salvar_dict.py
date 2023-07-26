import json


class Disciplina:
    def __init__(self, nome, ch) -> None:
        self.nome = nome
        self.carga_horaria = ch
        self.professor = None
        self.alunos = list()

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

    def add_professor(self, professor):
        self.professor = professor


disciplina = Disciplina("POO", 80)
disciplina.add_professor("Thomaz")
disciplina.add_aluno("Luan")
disciplina.add_aluno("Emilly")
disciplina.add_aluno("Ruan")
disciplina.add_aluno("Hiago")
nome = disciplina.nome
ch = disciplina.carga_horaria
prof = disciplina.professor
alunos = disciplina.alunos
D = {"nome": nome, "carga_horaria": ch, "professor": prof, "alunos": alunos}

with open("minha_disciplina.json", "w") as f:
    json.dump(D, f)
