# Revisão:
# Definição de strings
# Como acessar elementos
# Fatiamento (slicing)
# Operações em strings: + e *

# Hoje:
# Métodos de strings

# 1. uper() e lower(): convertem os elementos da string para maiusculo e minusculo
print("----- uper() e lower()")
str = "Cena Oculta"
nova_str = str.upper()
print( nova_str )
print( str.lower() )

# 2. split(): Divide uma string em substrings com base em um separador e retorna uma lista
print("----- split()")
str = "Todo mundo odeia O john"

lista_de_palavras = str.split('o')

print(lista_de_palavras)

# 3. join(): Junta elementos de uma lista em uma única string usando uma outra string como separador/juntador.
print("----- join()")
lista_de_palavras = ['Cena', 'Oculta', 'Foi', 'O', 'Melhor', 'Filme']
separador = '-NÃO-'
nova_string = separador.join(lista_de_palavras)
print(nova_string)

# 4. capitalize(): Converte o primeiro caractere para maiúsculo e deixa os demais minúsculos
print("----- capitaliza()")
str = "CONVERGENTE foi o FILME MAIS origGINAL"
print(str.capitalize())

# 5. replace(): Substitui um determinado trecho da string por outro
print("----- replace()")
str = "Cena Oculta foi o MELHOR filme de todos"

nova_str = str.replace('Cena Oculta', 'Antes que Esfrie')

print(nova_str)

# 6. count(): conta o número de vezes que um determinado caractere aparece na string
print("----- count()")
str = "Todo mundo odeia O john"
quantidade = str.count('o')

print(quantidade)

# 7. find() e index(): ambos retornam o índice da primeira ocorrência de um determinado caractere. Caso o caractere não exista, o find retorna -1 e o index dá erro.
str = "Cena Oculta"
print("----- find() e index()")

indice1 = str.find('a')
indice2 = str.index('a')

print(indice1)
print(indice2)

# 8. 
str = "CenaOculta"
print(str.isdecimal)