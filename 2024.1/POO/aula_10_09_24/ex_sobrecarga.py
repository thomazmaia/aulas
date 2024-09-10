# Sobrecarga de operador

class Ponto:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)
    
    # def __repr__(self) -> str:
    #     return f"({self.x},{self.y})"
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
    def __eq__(self, value: object) -> bool:
        if self.x == value.x and self.y == value.y:
            return True
        return False

PA = Ponto(1, 2)
PB = Ponto(1, 2)

novo_ponto = PA + PB # (4, 6)
print(novo_ponto)

if PA == PB:
    print("Os pontos são os mesmos")
else:
    print("São pontos diferentes")