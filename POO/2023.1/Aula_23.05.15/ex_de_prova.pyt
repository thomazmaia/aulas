class Azul:
    cor = "azul"
    nivel = 1
    tom = "marinho"

    def eh_vermelho(self):
        return False


class Vermelho:
    cor = "vermelho"
    nivel = 2

    def eh_vermelho(self):
        return True


class Minha:
    def printcor(self):
        print(self.cor)
        print(self.nivel)
        print(self.tom)


class MinhaCor(Minha, Vermelho, Azul):
    def eh_vermelho(self):
        return "Sempre!"


mc = MinhaCor()
mc.printcor()
print(mc.eh_vermelho())
