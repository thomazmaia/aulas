# Crie uma classe base (mãe) chamada Animal que possue o método falar() que imprime a mensagem "O animal está emitindo sons". Em seguida, crie uma subclasse (filha) chamda Cachorro, que herda de Animal. A classe Cachorro deve sobrescrever o método falar() para imprimir a mensagem "O cachorro está latindo".

class Animal:
    def falar(self):
        print("O animal está emitindo sons.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro está latindo.")

A = Animal()
C = Cachorro()

A.falar()
C.falar()