def encontra_mais_longa(texto : str):
    lista_de_palavras = texto.split()
    aux = 0
    maior_palavra = ''
    for palavra in lista_de_palavras:
        tamanho = len(palavra)
        if tamanho > aux:
            aux = tamanho
            maior_palavra = palavra
            
    return maior_palavra


entrada = "Esta é uma frase para encontrar a palavra mais longa."
saida = encontra_mais_longa(entrada)
print(f"Maior palavra: {saida}")