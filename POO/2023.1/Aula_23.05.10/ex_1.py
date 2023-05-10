class Animal:
    def falar(self):
        print("O animal está emitindo sons.")


class Cachorro(Animal):
    def falar(self):
        print("O cachorro está latindo")


gato = Animal()
gato.falar()

dog = Cachorro()
dog.falar()
