def tira_espaco(texto : str):
    lista_de_strings = texto.split()
    res = " ".join(lista_de_strings)
    return res


entrada = "Olá, mundo!      Este é um exemplo."
saida = tira_espaco(entrada)

print(saida)