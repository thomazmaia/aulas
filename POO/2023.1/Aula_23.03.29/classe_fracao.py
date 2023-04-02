class Fracao:
    def __init__(self, numerador, denominador) -> None:
        self.num = int(numerador)
        self.den = int(denominador)
        self.res = 0

    # GETTER
    @property
    def res(self):
        return f"{self.num}/{self.den} = {self.num/self.den}"
    
    @res.setter
    def res(self, valor):
        self._res = valor




    @property
    def den(self):
        return self._den
    
    @den.setter
    def den(self, valor):
        if valor != 0:
            self._den = valor  
                

F = Fracao(1, 2)
print(F.res)

F.den = 0
print(F.res)