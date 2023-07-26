class Turma:
    def __init__(self, num_alunos) -> None:
        self.num_alunos = num_alunos

    def __add__(self, nova_sala):
        return self.num_alunos + nova_sala.num_alunos

    def __gt__(self, nova_turma):
        if self.num_alunos > nova_turma.num_alunos:
            return True
        return False


s5 = Turma(10)
s1 = Turma(40)

if s1 < s5:
    print("Coloca o S5 no lab maior")
else:
    print("Coloca o S5 no lab menor")