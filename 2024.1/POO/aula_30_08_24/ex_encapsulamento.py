class BancoDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        self.__dados[id] = nome
        print(f"[{nome}] cadastrado com sucesso")

    def apagar_cliente(self, id):
        x = self.__dados[id]
        del self.__dados[id]
        print(f"[{x}] apagado com sucesso")

    def listar_clientes(self):
        print("## CLIENTES CADASTRADOS:")
        print("------------------------")
        for id, nome in self.__dados.items():
            print(f"[{id}] {nome}")


bd = BancoDeDados()
bd.inserir_cliente(1, "Thomaz")
bd.inserir_cliente(2, "Yasmim")
bd.inserir_cliente(3, "João Victor")
bd.inserir_cliente(4, "João Paulo")

bd.listar_clientes()

bd.__dados = "uma string"

bd.listar_clientes()