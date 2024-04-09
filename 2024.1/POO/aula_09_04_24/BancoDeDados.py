class BancoDeDados:
    def __init__(self) -> None:
        self.__dados = dict()

    def inserir_cliente(self, id, nome):
        flag = False
        for meu_id in self.__dados.keys():
            if self.__dados[meu_id] == nome:
                print(f"Usuário já cadastrado na id {meu_id}")
                flag = True
        if flag == False:
            print(f"Inserindo cliente '{nome}'")
            self.__dados[id] = nome

    def apagar_cliente(self, id):
        print(f"Apagando cliente '{self.__dados[id]}'")
        del self.__dados[id]

    def listar_clientes(self):
        print("Listando clientes...")
        for id, nome in self.__dados.items():
            print(f"[{id}] - {nome}")


bd = BancoDeDados()
bd.inserir_cliente(0, "Thomaz")
bd.inserir_cliente(1, "Thomaz")
bd.inserir_cliente(2, "JV")
bd.inserir_cliente(3, "Yas")

bd.listar_clientes()