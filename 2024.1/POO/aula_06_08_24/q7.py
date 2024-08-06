class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatar_data(self):
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano}"
    
    def eh_valida(self):
        dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.__ano % 4 == 0 and self.__ano % 100 != 0:
            dias[1] = 29
        if self.__mes < 1 or self.__mes > 12:
            print("Mês inválido!")
        elif self.__dia < 1 or self.__dia > dias[self.__mes - 1]:
            print("Dia inválido")


d = Data(29, 2, 1988)
print(d.formatar_data())
d.eh_valida()