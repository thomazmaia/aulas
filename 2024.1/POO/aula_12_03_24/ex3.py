# Classe ControleRemoto
# • Atributos: ligada (Bool), canal (int), volume (int)
# • Métodos: ligar(), desligar(), canal_mais(), canal_menos(), aumentar_volume(), diminuir_volume()

class ControleRemoto:
    def __init__(self) -> None:
        self.ligada = False
        self.canal = 1
        self.volume = 1

    def ligar(self):
        print("TV ligada")
        self.ligada = True

    def desligar(self):
        self.ligada = False
        print("TV desligada")

    def canal_mais(self):
        if self.ligada == True:
            if self.canal == 12:
                self.canal = 1
            else:
                self.canal += 1

    def canal_menos(self):
        if self.ligada == True:
            if self.canal == 1:
                self.canal = 12
            else:
                self.canal -= 1

    def aumentar_volume(self):
        if self.ligada == True:
            self.volume += 1

    def diminuir_volume(self):
        if self.ligada == True:        
            self.volume -= 1



CR = ControleRemoto()
CR.ligar()
while True:
    print("1 - Canal menos")
    print("2 - Canal mais")
    print("3 - Desligar")
    op = int(input("Opção: "))
    if op == 1:
        CR.canal_menos()
    elif op == 2:
        CR.canal_mais()
    elif op == 3:
        CR.desligar()
    elif op == 5:
        break
    print(f"Canal atual: {CR.canal}")