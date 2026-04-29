# Strings: são sequências de caracteres (letras, números, símbolos, espaço) que podem ser aramzenadas em uma vairável. São definidas por aspas (simples ou duplas).
# Ex:
# var = "Olá Mundo"
# var = 'Olá Mundo'

# Indexação
# Uma string pode conter zero ou mais elementos e o tamanho da string é igual à quantidade de elementos que ela contém. Cada caractere (letra, número, símbolo) é um elemento.
# O acesso aos caracteres/elementos pode ser feito por INDEXAÇÃO em que cada caractere está numa posição que é representada por um número (índice) começando de zero.
str = " MARIA 1 "
for i in range(9):
    print(str[i])

# Tamanho da String
# A função 'len' recebe uma string como argumento e retorna o tamanho dessa string. Ou seja, a quantidade de caracteres dela.
# Ex:
# len("Maria") -> 5
# len("123") -> 3
# len("Olá Mundo") -> 9