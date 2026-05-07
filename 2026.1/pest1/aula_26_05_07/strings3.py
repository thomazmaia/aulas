# Fatiamento (slicing) de strings
# Serve para criar uma nova string a partir de uma fatia (ou substring) da string original.
# string[inicio : fim : passo]

str = "Abacaxi"
#.     0123456
print(str[0]) # 'A'
print(str[len(str)-1]) # 'i'
print(str[4]) # 'a'
print("-------------")
print(str[0 : 3]) # Índice 0, 1, 2 - Aba
print(str[3:7]) # 'caxi'
print(str[3:]) # 'caxi'
print(str[:3]) # 'Aba'
print(str[:]) # 'Abacaxi'
print("-------------")
str = "Abacaxi"
#.     0123456
print(str[0:7:2]) # 'Aaai'
print(str[::2]) # 'Aaai'
print(str[::3]) # 'Aci'
print(str[6:2:-1]) # 'ixac'
print(str[::-1]) # 'ixacabA'