# STRINGS
# Strings são uma sequência de caracteres (letras, números, símbolos e espaços) que podem ser armazenados em uma variável. Elas são representadas por aspas (simples ou duplas).
str1 = "isso é uma string"
str2 = 'isso é uma string'
str3 = "isso é 'uma' string"
str4 = 'isso é "uma" string'
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# FATIAMENTO DE STRINGS
# O fatiamento (slicing) permite extrair uma parte específica de uma string semelhante ao fatiamento de listas, onde é possível extrair uma parte específica da lista.
# Obedece às mesmas regras de indexação das listas.
L = ['uva', 99, 3.14, '_']
S = "uva993 14_"

print(L[0]) # Primeiro elemento da lista
print(S[0]) # Primeiro caractere/elemento da string

print(L[0:2]) # Os dois primeiros elementos da lista
print(S[0:2]) # Os dois primeiros caracteres/elementos da string

print(S[3:8]) # "993 1"

print(S[-1])  # Último caracere/elemento da string