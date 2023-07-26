class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao_em_minutos = duracao

    def exibir_duracao_em_horas(self):
        horas = int(self.duracao_em_minutos) // 60
        minutos = int(self.duracao_em_minutos) % 60
        print(f"O filme {self.titulo} possui {horas} horas e {minutos} minutos de duração")