class Livro:
    def __init__(self, titulo:str, autor:str, ano:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano

    def mostrar_detalhes(self):
        print("--- INFORMAÇÕES ---")
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor} - Ano de publicação: {self.__ano_publicacao}")
        print("-------------------")

o_senhor_dos_aneis = Livro("O Senhor dos Aneis", "JRR Tolkien", 1954)
livro2 = Livro("Um titulo qualquer", "Fulano de tal", 2024)

o_senhor_dos_aneis.mostrar_detalhes()
livro2.mostrar_detalhes()