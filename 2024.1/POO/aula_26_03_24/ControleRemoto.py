class ControleRemoto:
    def __init__(self, ligada : bool, canal : int, volume : int) -> None:
        self.ligada = ligada
        self.canal = canal
        self.volume = volume

    def ligar(self):
        if self.ligada == False:
            print("Ligando a TV...")
            self.ligada = True
        else:
            print("A TV já está ligada!")
    
    def desligar(self):
        if self.ligada == True:
            print("Desligando a TV...")
            self.ligada = False
        else:
            print("A TV já está desligada!")
    
    def canal_mais(self):
        if self.ligada == True:
            self.canal += 1
            print(f"Aumentando canal para {self.canal}")
        else:
            print("Ligue a TV primeiro.")
    
    def canal_menos(self):
        if self.ligada == True:
            self.canal -= 1
            print(f"Diminuindo canal para {self.canal}")
        else:
            print("Ligue a TV primeiro.")
    
    def aumentar_volume(self):
        if self.ligada == True:
            self.volume += 1
            print(f"Aumentando volume para {self.volume}")
        else:
            print("Ligue a TV primeiro.")
    
    def diminuir_volume(self):
        if self.ligada == True:
            self.volume -= 1
            print(f"Diminuindo volume para {self.volume}")
        else:
            print("Ligue a TV primeiro.")
