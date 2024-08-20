class Produto:
    def __init__(self, nome:str, valor:float) -> None:
        self.nome = nome
        self.valor = valor


class Carrinho:
    def __init__(self) -> None:
        self.produtos = []

    def inserir_produto(self, P:Produto):
        self.produtos.append(P)

    def listar_produtos(self):
        print("Listando produtos...")
        if len(self.produtos) == 0:
            print("...carrinho vazio...")
        else:
            for produto in self.produtos:
                print(f"{produto.nome} R$ {produto.valor}")
        print("--------------------")


P1 = Produto("Arroz", 4.99)
P2 = Produto("Feijao", 3.50)
P3 = Produto("Açúcar", 3.00)
P4 = Produto("Batata", 1.99)

C = Carrinho()
C.listar_produtos()
C.inserir_produto(P2)
C.inserir_produto(P4)
C.inserir_produto(P1)
C.inserir_produto("thomaz")
C.listar_produtos()