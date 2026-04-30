# Strings: são sequências de caracteres (letras, números, símbolos, espaço) que podem ser aramzenadas em uma vairável. São definidas por aspas (simples ou duplas).
# Ex:
# var = "Olá Mundo"
# var = 'Olá Mundo'

# Indexação
# Uma string pode conter zero ou mais elementos e o tamanho da string é igual à quantidade de elementos que ela contém. Cada caractere (letra, número, símbolo) é um elemento.
# O acesso aos caracteres/elementos pode ser feito por INDEXAÇÃO em que cada caractere está numa posição que é representada por um número (índice) começando de zero.

str = "ABACAXI"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])

# EX: Crie um código para ler uma string do usuário e mostre todos os seus caracteres, linha a linha.
string_do_usuario = input("Digite: ")

tamanho = len(string_do_usuario)

for i in range(tamanho):
    print(string_do_usuario[i])

# Tamanho da String
# A função LEN retorna o tamanho de coleções.
# Ex:
# str = "Olá Mundo"
# tam = len(str)
# print(tam)