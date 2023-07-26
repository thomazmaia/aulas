class Cachorro:
    # Função "construtora"
    def __init__(self):
        # Atributos
        self.estado_atual = "Vivo"

    # Métodos
    def latir(self):
        self.estado_atual = "Latindo"

    def comer(self):
        self.estado_atual = "Comendo"

    def morder(self):
        self.estado_atual = "Mordendo"


# Instanciamento da classe (criação do objeto 'dog')
dog = Cachorro()
print(f"Estado atual do dog: {dog.estado_atual}")
dog.comer()
print(f"Estado atual do dog: {dog.estado_atual}")