# 1. Escreva uma função em Python chamada primeiro_e_ultimo que receba uma string como entrada e retorne uma nova string contendo apenas o primeiro e o último caractere da string original.

def primeiro_e_ultimo(texto : str):
    primeiro = texto[0]
    tamanho = len(texto)
    ultimo = texto[tamanho-1] # texto[-1]
    nova_string = primeiro + ultimo
    return nova_string


nova = primeiro_e_ultimo("Abacaxi")
print(nova)