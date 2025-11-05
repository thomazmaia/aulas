# Escreva uma função em Python chamada "primeiro_e_ultimo" que recebe uma string como entrada e retorna uma nova string contendo apenas o primeiro e o último caractere da string original.
# Ex:
# primeiro_e_ultimo("Python") deve retornar "Pn"

def primeiro_e_ultimo(string : str):
    primeiro = string[0]
    ultimo = string[len(string)-1]
    nova_string = primeiro + ultimo
    return nova_string


print(primeiro_e_ultimo("Python"))
print(primeiro_e_ultimo("Abacaxi"))