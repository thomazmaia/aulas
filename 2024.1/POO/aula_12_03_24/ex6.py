# Classe Carro
# • Atributos: modelo (str), ano (int), cor (str), velocidade (float), velocidade_max (float)
# • Métodos: imprimir(), acelerar(float), parar()

class Carro:
    def __init__(self, mod : str, ano : int, cor : str, vmax : float) -> None:
        self.modelo = mod
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_maxima = vmax

    def imprimir(self):
        print(f"{self.modelo} ano {self.ano} cor {self.cor}")

    def acelerar(self, x : float):
        if (self.velocidade + x) > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima
        else:
            self.velocidade += 25
    

    def parar(self):
        for i in range(self.velocidade, -1, -1):
            self.velocidade = i
            print(f"Freando... {self.velocidade} km/h")


fit = Carro("Honda", 2023, "Branco", 200)
fit.imprimir()

gol = Carro("VW", 2000, "Preto", 150)

while True:
    print("0 - Sair")
    print("1 - Acelerar")
    print("2 - Parar")
    op = int(input("Opção: "))
    if op == 0:
        break
    elif op == 1:
        gol.acelerar(5)
        print(f"Velocidade atual: {gol.velocidade} km/h")
    elif op == 2:
        gol.parar()
        print(f"Velocidade atual: {gol.velocidade} km/h")