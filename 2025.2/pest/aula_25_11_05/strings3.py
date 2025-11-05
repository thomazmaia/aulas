# OPERAÇÕES COM STRINGS
# Strings são IMUTÁVEIS. Você não pode modificar um caractere da string.
# S = 'abacaxu'
# S[6] = 'i' # erro
# print(S)

# 1 - Operação de soma/união/concatenação
str1 = 'aba'
str2 = 'caxi'

str3 = str1 + str2
print(str3)

# 2 - Operação de multiplicação/repetição
str = "vozão "

nova_str = 3 * str
print(nova_str)

# Exercício: Corrija a string 'abacaxu'
S = 'abacaxu'
S = S[:6] + 'i'

print(S)