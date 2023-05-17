class Ingresso:
    def __init__(self, val) -> None:
        self.valor = val

    def imprime_valor(self):
        print(f"Valor do ingresso: {self.valor}")


class VIP(Ingresso):
    def __init__(self, val) -> None:
        super().__init__(val + 0.5 * val)


ing = Ingresso(50)
ing_vip = VIP(ing.valor)

ing.imprime_valor()
ing_vip.imprime_valor()
