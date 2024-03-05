class Passaro:
    # Inicializador ("construtor") da classe
    def __init__(self):
        # Atributos
        self.quantidade_de_pernas = 2
        self.quantidade_de_olhos = 2
        self.quantidade_de_bicos = 1
        self.possui_penas = True
        self.estado_atual = "Não nasceu"
        self.estomago = list()

    # Métodos
    def voar(self):
        print("Estou voando")
        self.estado_atual = "Voando"

    def andar(self):
        print("Estou andando")
        self.estado_atual = "Andando"

    def comer(self, tipo_de_comida):
        print("Estou comendo")
        self.estado_atual = "Comendo"
        self.estomago.append(tipo_de_comida)


papagaio = Passaro()
coruja = Passaro()

print(f"Estomago do papagaio antes de comer: {papagaio.estomago}")
papagaio.comer("manga")
papagaio.comer("abacaxi")
papagaio.comer("alpiste")
print(f"Estomago do papagaio depois de comer: {papagaio.estomago}")

print(f"Estomago da coruja antes de comer: {coruja.estomago}")
coruja.comer("biscoito de chocolate")
print(f"Estomago da coruja depois de comer: {coruja.estomago}")