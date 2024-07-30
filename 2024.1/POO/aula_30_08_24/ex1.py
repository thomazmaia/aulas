# 1. Crie uma classe chamada `Cachorro` com os atributos `nome`, `raca` e `idade`. Crie um objeto da classe `Cachorro` chamado **rex** com os seguintes valores para os atributos:
# - nome: Rex
# - raca: Pastor Alemão
# - idade: 3

class Cachorro:
    def __init__(self, nome : str, raca : str, idade : int):
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade


rex = Cachorro("Rex", "Pastor Alemão", 3)