# Crie uma classe chamada Produto com os atributos nome, preco e quantidade. Crie métodos getters e setters para cada atributo. Crie um objeto da classe Produto chamado produto1 e atribua os seguintes valores aos atributos:
# - nome: Televisão
# - preco: 2000
# - quantidade: 10
# Utilize os métodos getters e setters para modificar o preço do produto para R$1800 e a quantidade para 5. Imprima os valores atualizados dos atributos do objeto produto1.

class Produto:
    def __init__(self, nome:str, preco:float, qtd:int):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = qtd

    # Setters:
    def set_nome(self, nome:str):
        self.__nome = nome

    def set_preco(self, preco:float):
        self.__preco = preco

    def set_quantidade(self, qtd:int):
        self.__quantidade = qtd

    # Getters:
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    


produto1 = Produto("Televisão", 2000, 10)

produto1.set_preco(1800)
produto1.set_quantidade(5)

print(produto1.get_nome())
print(produto1.get_preco())
print(produto1.get_quantidade())