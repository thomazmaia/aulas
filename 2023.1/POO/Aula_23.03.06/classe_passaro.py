''''
    Aula_23_03_06
'''

class Passaro: 
    estado_atual = 'Morto!' 

    def __init__(self): 
        self.quantidade_de_pernas = 2 
        self.quantidade_de_olhos = 2 
        self.quantidade_de_bicos = 1 
        self.tem_pena = True 
        self.estado_atual = 'Vivo :)' 
        self.estomago = []
    
    def voar(self): 
        self.estado_atual = 'Voando' 
        print("Estou voando")
    
    def andar(self): 
        self.estado_atual = 'Andando' 
        print("Estou andando")
    
    def comer(self): 
        self.estado_atual = 'Comendo' 
        self.estomago.append('comida')
        print("Estou comendo")


P1 = Passaro()
P1.comer()
print(P1.estomago)

P2 = Passaro() 
#P2.comer() 
print(P2.estomago)