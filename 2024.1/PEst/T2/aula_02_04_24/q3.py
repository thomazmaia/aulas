# 3. Escreva uma função chamada reverter que aceite uma string como entrada e retorne a string revertida.

def reverter(str : str):
    return str[-1::-1]

print(reverter("Abacaxi"))