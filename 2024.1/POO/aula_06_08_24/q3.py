class Produto:
    def __init__(self, nome:str, preco:float, estoque:int):
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_estoque(estoque)

    # Getters:
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    
    # Setters:
    def set_nome(self, nome):
        self.__nome =  nome
    def set_preco(self, preco):
        self.__preco = preco
    def set_estoque(self, estoque):
        self.__estoque = estoque


produto1 = Produto("Camiseta", 25, 100)
produto1.set_preco(30)
produto1.set_estoque(50)