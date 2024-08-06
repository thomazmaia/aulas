class Aluno:
    todos_os_alunos = list()

    def __init__(self, nome:str, idade:int, notas:list):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        self.todos_os_alunos.append(self)

    def media_notas(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        return soma/len(self.notas)
    
    @classmethod
    def quantidade_alunos(cls):
        return len(cls.todos_os_alunos)
    
    @classmethod
    def aluno_mais_velho(cls):
        maior_idade = 0
        maior_pessoa = ""
        for aluno in cls.todos_os_alunos:
            if aluno.idade > maior_idade:
                maior_idade = aluno.idade
                maior_pessoa = aluno.nome
        return maior_pessoa
    
    @staticmethod
    def nota_media():
        return 6.0



a1 = Aluno("Yasmin", 27, [6, 7, 8])
a2 = Aluno("João Victor", 17, [8, 8.3, 9])
a3 = Aluno("Lara", 17, [7.8, 7.9, 8.5])
a4 = Aluno("João Paulo", 18, [5.5, 6, 4.5, 7])

if a1.media_notas() >= a1.nota_media():
    print(f"{a1.nome} passou!")