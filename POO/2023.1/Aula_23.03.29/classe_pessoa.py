class Pessoa:
    def __init__(self):
        self._nome = ""

    @property   # GETTER DE nome 
    def nome_completo(self):
        return f"Nome: {self.nome_completo}"

    @nome_completo.setter # SETTER DE nome
    def nome_completo(self, nome_que_colocaram):
        aux = nome_que_colocaram.split()
        if len(aux) > 1:
            self._nome = nome_que_colocaram





P = Pessoa()

P.nome_completo = "Thomaz Maia"
print(P.nome_completo)

P.nome_completo = "Fulano"
print(P.nome_completo)

P.nome_completo = "Fulano de TAL"
print(P.nome_completo)