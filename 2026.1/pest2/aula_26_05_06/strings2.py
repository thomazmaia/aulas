# Acessando elementos
str = "Abacaxi"

for i in range(len(str)):
    print(i, str[i])

print(20 * "-")

for caractere in str:
    print(caractere)


# Operações com strings
# -> Strings são IMUTÁVEIS (não podem ser modificadas depois de criadas)
# 1. Soma (concatenação): ao "somar" duas strings, você está na verdade concatenando (juntando) duas strings e criando uma nova.
str = "Abacaxi"
str2 = "@" + "bacaxi"

print(str)
print(str2)

# 2. Produto (repetição): ao "multiplicar" uma string por um número N, você está na verdade repetindo a string N vezes.

str = "IFCE"
res = 5 * str

print(res)