class Ingresso:
    def __init__(self, val) -> None:
        self.valor = val

    def imprime_valor(self):
        print(f"Valor do ingresso: {self.valor}")


class VIP(Ingresso):
    def __init__(self, val) -> None:
        super().__init__(val + 0.5 * val)


valor = float(input("Digite o valor do ingresso? "))
ing = Ingresso(valor)
ing_vip = VIP(ing.valor)

ing.imprime_valor()
ing_vip.imprime_valor()
