def get_palavra_mais_longa(texto : str):
    lista_de_palavras = texto.split()
    tamanho_maior = 0
    palavra_maior = ''
    for palavra in lista_de_palavras:
        tamanho_atual = len(palavra)
        if tamanho_atual > tamanho_maior:
            tamanho_maior = tamanho_atual
            palavra_maior = palavra
    return palavra_maior
    


entrada = "Esta é umaaaaaaaaaaaa frase para encontrar a palavra mais longa."
saida = get_palavra_mais_longa(entrada)

print(saida)