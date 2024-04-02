# 4. Crie uma função chamada `saltos` que receba uma string e um número inteiro positivo como entrada, representando o tamanho do salto, e retorne uma nova string contendo apenas os caracteres da string original que estão nos índices múltiplos do tamanho do salto.
# Ex: `saltos("Python Programming", 3)`  deve retornar "Ph oai”

def saltos(str : str, tamanho : int):
    return str[::tamanho]


print(saltos("Python Programming", 3))