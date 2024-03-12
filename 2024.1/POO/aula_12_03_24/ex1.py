#Classe Cachorro
#• Atributos: estado_atual (str)
#• Métodos: latir(), comer(), morder()


class Cachorro:
    def __init__(self) -> None:
        self.estado_atual = None
    
    def latir(self):
        self.estado_atual = "Latindo"
        print("Au au au!")

    def comer(self):
        self.estado_atual = "Comendo"
        print("Nham nham!")

    def morder(self):
        self.estado_atual = "Mordendo"
        print("NHAC!")


toto = Cachorro()
fifi = Cachorro()

toto.comer()
fifi.latir()

print(toto.estado_atual)
print(fifi.estado_atual)