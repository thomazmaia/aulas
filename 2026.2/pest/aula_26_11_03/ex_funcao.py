# Funções em Python:
# São blocos de códigos que podem ser chamados repetidas vezes ao longo do seu programa. Eles servem para modularizar seu código evitando códigos repetidos. As funções deixam os códigos organizados evitando erros.

# Sintaxe de funções:
# def nome_da_funcao(parâmetros):
#   corpo da função

def qual_idade(nome, idade):
    x = idade * 365
    print(f"{nome} tem {idade} anos de vida")
    print(f"{nome} tem {x} dias de vida")


qual_idade("mayra", 17)
qual_idade("samuel", 16)
qual_idade("thomaz", 38)