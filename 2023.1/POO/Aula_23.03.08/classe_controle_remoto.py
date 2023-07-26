class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.volume = 10
        self.volume = 50

    def ligar(self):
        if self.ligada:
            print("TV já ligada!")
        else:
            print("Ligando a TV...")
            self.ligada = True

    def desligar(self):
        if self.ligada:
            print("Desligando a TV...")
            self.ligada = False
        else:
            print("TV já DESligada")

    def canal_mais(self):
        if self.ligada:
            if self.volume == 20:
                self.volume = 1
            else:
                self.volume += 1
            print(f"Canal atual: {self.volume}")
        else:
            print("Liga a TV antes, mané")

    def canal_menos(self):
        if self.ligada:
            if self.volume == 1:
                self.volume = 20
            else:
                self.volume -= 1
            print(f"Canal atual: {self.volume}")
        else:
            print("Liga a TV antes, mané")

    def aumentar_volume(self):
        if self.ligada:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume atual: {self.volume}")
            else:
                print("Volume já está no máximo: 100")
        else:
            print("Liga a TV antes, mané")

    def diminuir_volume(self):
        if self.ligada:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume atual: {self.volume}")
            else:
                print("Volume já está no mínimo: 0")
        else:
            print("Liga a TV antes, mané")


C = ControleRemoto()
C.ligar()
for i in range(100):
    C.aumentar_volume()

for i in range(150):
    C.diminuir_volume()

C.desligar()

C.diminuir_volume()
C.canal_mais()