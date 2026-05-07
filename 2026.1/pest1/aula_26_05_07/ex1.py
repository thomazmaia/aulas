# Cria uma função que receba uma string e retorna uma nova string formada pelo primeiro e o último caractere da string recebida.
# Ex: 'Abacaxi' -> 'Ai'

def minha_funcao(string : str):
    char1 = string[0]
    char2 = string[len(string)-1]
    nova_string = char1 + char2
    return nova_string


print(minha_funcao("Uva"))