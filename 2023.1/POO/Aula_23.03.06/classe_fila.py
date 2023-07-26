''''
    Aula_23_03_06
'''

class Fila:
    def __init__(self):
        self.fila = []

    def aumentar(self, pessoa):
        self.fila.append(pessoa)

    def diminuir(self):
        self.fila.pop(0)


supermercado = Fila()
supermercado.aumentar("Lana")
supermercado.aumentar("Luan")
supermercado.aumentar("Emilly")
supermercado.aumentar("André")
print(supermercado.fila)
supermercado.fila.append("ALGUEM")
print(supermercado.fila)