class RetanguloPrimitivo:
    def __init__(self, x, y, tam_x, tam_y) -> None:
        self.x = x
        self.y = y
        self.tamanho_x = tam_x
        self.tamanho_y = tam_y


class RedimensaoMixin:
    def redimensionar(self, novo_tam_x, novo_tam_y):
        self.tamanho_x = novo_tam_x
        self.tamanho_y = novo_tam_y


class Retangulo(RetanguloPrimitivo, RedimensaoMixin):
    pass


R = Retangulo(0, 0, 50, 10)
R.redimensionar(5, 1)
