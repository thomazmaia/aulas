class Fila:
    def __init__(self) -> None:
        self.fila = list()
        self.quantidade_de_pessoas = len(self.fila)

    def aumentar(self, nome):
        self.fila.append(nome)
        self.quantidade_de_pessoas = len(self.fila)

    def diminuir(self):
        self.fila.pop(0)

    def mostrar_fila(self):
        for i in range (len(self.fila)):
            print(f"{i+1}o: {self.fila[i]}")



F = Fila()
F.aumentar("Thomaz")
F.aumentar("Yasmim")
F.aumentar("JV")
F.mostrar_fila()
F.diminuir()
F.aumentar("Lara")
F.mostrar_fila()

G = Fila()
G.aumentar("Thomaz")
G.mostrar_fila()