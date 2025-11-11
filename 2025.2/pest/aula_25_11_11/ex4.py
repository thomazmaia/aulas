# Crie uma função chamada saltos que receba uma string e um número inteiro positivo como entrada, representando o tamanho do salto, e retorne uma nova string contendo apenas os caracteres da string original que estão nos índices múltiplos do tamanho do salto.

# Ex: saltos("Python Programming", 3) deve retornar "Ph oai”

def saltos(string : str, tamanho : int):
    nova_string = string[::tamanho]
    return nova_string


print(saltos("Python Programming", 3))
print(saltos("Abacaxi e uva", 2))