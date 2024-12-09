# Indexação de strings
# Os caracteres de uma string podem ser acessados através de índices. O primeiro elemento da string é o índice 0 (zero), o segundo é o índice 1, e assim por diante.

str = "caneta"

print(f"Primeira letra: {str[0]}")
print(f"Segunda letra: {str[1]}")
print(f"terceira letra: {str[2]}")
print(f"quarta letra: {str[3]}")
print(f"quinta letra: {str[4]}")
print(f"sexta letra: {str[5]}")
# print(str[6]) # ERRO

# Acessando elementos
# 1a) Com WHILE
str = "caneta"
indice = 0
while indice < len(str):
    print(str[indice])
    indice = indice + 1

# 2a) com FOR
str = 'qualquer outra coisa'
for indice in range(0, len(str), 1):
    print(str[indice])

# 3a) com FOR (sem índice)
str = "caneta"
for item in str:
    print(item)