class RetanguloPrimitivo:
    def __init__(self, x:int, y:int, tx:int, ty:int):
        self.x = x
        self.y = y
        self.tamanho_x = tx
        self.tamanho_y = ty

class RedimensaoMixin:
    def redimensionar(self, tx:int, ty:int):
        self.tamanho_x = tx
        self.tamanho_y = ty


class Retangulo(RetanguloPrimitivo, RedimensaoMixin):
    def mostra_tamanho(self):
        print(self.tamanho_x, self.tamanho_y)


R = Retangulo(10, 10, 480, 320)
R.redimensionar(260, 160)
R.mostra_tamanho()