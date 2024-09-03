class Azul:
    cor = "azul"
    nivel = 1
    tom = "Marinho"

    def eh_vermelho(self):
        return False

class Vermelho:
    cor = "Vermelho"
    nivel = 2

    def eh_vermelho(self):
        return True

class Minha:
    def printcor(self):
        print(self.cor)
        print(self.nivel)
        print(self.tom)

class MinhaCor(Azul, Vermelho, Minha):
    def eh_vermelho(self):
        return "Sempre"
    

mc = MinhaCor()
mc.printcor()
print(mc.eh_vermelho())