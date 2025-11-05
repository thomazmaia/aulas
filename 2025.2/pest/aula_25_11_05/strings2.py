# ACESSANDO ELEMENTOS DE UMA STRING
# Assim como as listas, os elementos de uma string podem ser acessados elemento a elemento ou pelo índice. A função LEN funciona da mesma forma.

str = "Isso é uma string"

print("Forma 1:")
tamanho_da_str = len(str)
for i in range(tamanho_da_str):
    print(str[i])

print("Forma 2:")
for caractere in str:
    print(caractere)

# Exercício: crie um código para mostrar todos os caracteres de uma string DE TRÁS PARA FRENTE.
S = "ABACAXI"

print("Forma 1: slicing/fatiamento")
print(S[::-1])

print("Forma 2: laço for")
for i in range(len(S)-1, -1, -1):
    print(S[i])