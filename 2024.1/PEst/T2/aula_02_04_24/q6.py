# 6. Implemente uma função chamada letras_alternadas que receba uma string como entrada e retorne uma nova string contendo apenas os caracteres nos índices pares da string original.

def letras_alternadas(str : str):
    return str[::2]

print(letras_alternadas("Abacaxi"))