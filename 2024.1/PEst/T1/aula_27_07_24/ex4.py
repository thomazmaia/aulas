def remover_espacos(texto : str):
    # lista_de_palavras = texto.split()
    # texto_final = " ".join(lista_de_palavras)    
    return " ".join(texto.split())


entrada = "Olá, mundo!        Este é um exemplo."
saida = remover_espacos(entrada)

print(saida)