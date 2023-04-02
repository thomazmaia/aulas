class Elevador:
    def __init__(self, total, capacidade):
        self.inicializa(total, capacidade)

    def inicializa(self, total, capacidade):
        self.andar_atual = 0 # Térreo
        self.total_andares = total
        self.capacidade = capacidade
        self.pessoas = 0

    def entra(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
        else:
            print("Elevador lotado!")
        print(f"Total de pessoas: {self.pessoas}")

    def sai(self):
        if self.pessoas >= 1:
            self.pessoas -= 1
        else:
            print("Elevador vazio!")
        print(f"Total de pessoas: {self.pessoas}")

    def sobe(self):        
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print("Elevador na cobertura.")
        print(f"Andar atual: {self.andar_atual}")            

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print("Elevador no térreo.")
        print(f"Andar atual: {self.andar_atual}")            