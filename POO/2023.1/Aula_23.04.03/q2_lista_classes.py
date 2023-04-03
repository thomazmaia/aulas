class Livro:
    def __init__(self, titulo) -> None:
        self.__titulo = titulo
        self.__quantidade_de_paginas = 0
        self.__paginas_lidas = 0

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def quantidade_de_paginas(self):
        return self.__quantidade_de_paginas

    @quantidade_de_paginas.setter
    def quantidade_de_paginas(self, qtd):
        self.__quantidade_de_paginas = qtd

    @property
    def paginas_lidas(self):
        return self.__paginas_lidas

    @paginas_lidas.setter
    def paginas_lidas(self, pg):
        self.__paginas_lidas = pg

    def verificar_progresso(self):
        pc = self.__paginas_lidas*100/self.__quantidade_de_paginas
        print(f"Você já leu {pc} por cento do livro")


pequeno_principe = Livro("O Pequeno Príncipe")
pequeno_principe.quantidade_de_paginas = 98

print(f"O livro {pequeno_principe.titulo} possui {pequeno_principe.quantidade_de_paginas} páginas")

pequeno_principe.paginas_lidas = 20
pequeno_principe.verificar_progresso()
pequeno_principe.paginas_lidas = 50
pequeno_principe.verificar_progresso()