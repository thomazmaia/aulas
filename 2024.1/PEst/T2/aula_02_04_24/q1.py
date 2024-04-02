# 1. Escreva uma função em Python chamada primeiro_e_ultimo que receba uma string como entrada e retorne uma nova string contendo apenas o primeiro e o último caractere da string original.

def primeiro_e_ultimo(str : str):
    tamanho = len(str)
    primeiro = str[0]
    ultimo = str[tamanho-1]
    res = primeiro + ultimo
    return res


print(primeiro_e_ultimo("Abacaxi"))