class BancoDeDados:
    def __init__(self) -> None:
        self.__dados = dict()

    def inserir_cliente(self, id, nome):
        self.__dados[id] = nome

    def apagar_cliente(self, id):
        del self.__dados[id]

    def listar_clientes(self):
        print("Banco de dados:")
        for id, nome in self.__dados.items():
            print(id, nome)
        print("---------------")

BD = BancoDeDados()

BD.inserir_cliente(0, "Luan")
BD.inserir_cliente(1, "Emilly")
BD.inserir_cliente(2, "Hiago")
BD.inserir_cliente(3, "Ruan")
BD.inserir_cliente(10, "Andre")
BD.listar_clientes()
BD.apagar_cliente(10)
BD.listar_clientes()

BD._BancoDeDados__dados = "TCHAU"
BD.listar_clientes()