class Ingresso:
    def __init__(self, valor:float):
        self.valor = valor

    def imprime_valor(self):
        print(f"Falor do ingresso: R$ {self.valor}")


class VIP(Ingresso):
    def __init__(self, valor: float, valor_adicional:float):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def imprime_valor_vip(self):
        valor_vip = self.valor + self.valor_adicional
        print(f"Falor do ingresso VIP: R$ {valor_vip}")


bilhete = Ingresso(75)
bilhete_vip = VIP(75, 50)

bilhete.imprime_valor()
bilhete_vip.imprime_valor_vip()