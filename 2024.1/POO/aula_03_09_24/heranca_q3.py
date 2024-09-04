class Atleta:
    def __init__(self, peso:float) -> None:
        self.aposentado = False
        self.peso = peso

    def aposentar(self):
        print("Estou me aposentando...")
        self.aposentado = True

    def aquecer(self):
        if self.aposentado == False:
            print("Estou aquecendo...")
        else:
            print("Não posso. Estou aposentado!")


class Nadador(Atleta):
    def nadar(self):
        if self.aposentado == False:
            print("Estou nadando...")
        else:
            print("Não posso. Estou aposentado!")            

class Ciclista(Atleta):
    def pedalar(self):
        if self.aposentado == False:
            print("Estou pedalando...")
        else:
            print("Não posso. Estou aposentado!")   

class Corredor(Atleta):
    def correr(self):
        if self.aposentado == False:
            print("Estou correndo...")
        else:
            print("Não posso. Estou aposentado!")   

class Triatleta(Nadador, Ciclista, Corredor):
    pass

T = Triatleta(70)

T.aquecer()
T.nadar()
T.pedalar()
T.correr()

T.aposentar()

T.aquecer()
T.nadar()
T.pedalar()
T.correr()