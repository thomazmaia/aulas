class Jogador:
    def __init__(self, nome:str, numero:int, gols:int):
        self.__nome = nome
        self.__numero_camisa = numero
        self.__gols = gols

    def marcar_gol(self):
        self.__gols += 1

    def mostrar_gols(self):
        return self.__gols


messi = Jogador("Lionel Messi", 10, 750)
messi.marcar_gol()
messi.marcar_gol()
messi.marcar_gol()

print(messi.mostrar_gols())