class SuperLista:
    def __init__(self) -> None:
        self.__lis = []

    def __gt__(self, elemento):
        self.__lis.append(elemento)

    def __str__(self) -> str:
        for indice, item in enumerate(self.__lis):
            print(f"[{indice}] = {item}")
        return ""


teste = SuperLista()
print(teste)
teste > 9
teste > "oi"
teste > 92390393
print(teste)
