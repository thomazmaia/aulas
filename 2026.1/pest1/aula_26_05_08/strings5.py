# Métodos de strings

# 1. upper() - Converte uma string para maiúscula.
print("---------- upper() ----------")
str = "Todo Mundo Odeia o John"
nova_str = str.upper()
print(nova_str)

# 2. lower() - Converte uma string para minúscula.
print("---------- lower() ----------")
str = "Todo Mundo Odeia o John"
print(str.lower())

# 3. split() - Divide uma string em substrings com base em um separador e retorna uma LISTA.
print("---------- split() ----------")
frase = "Todo Mundo Odeia o John"

lista_de_palavras = frase.split()
print(lista_de_palavras)
for elemento in lista_de_palavras:
    print(elemento)

lista_de_palavras = frase.split('o')
print(lista_de_palavras)
for elemento in lista_de_palavras:
    print(elemento)

# 4. join() - Une elementos de uma lista em uma única string usando outra string como separador/juntador.
print("---------- join() ----------")
frase = "Todo Mundo Odeia o John"
lista = frase.split() # quebrei a frase em palavras
print(lista)

nova_frase = '-'.join(lista)
print(nova_frase)

# 5. capitalize() - Converte o primeiro caractere para maiúsculo
print("---------- capitalize() ----------")
frase = "Todo Mundo Odeia o John"
print(frase.capitalize())

# 6. replace() - Substitui um determinado trecho da string por outro.
print("---------- replace() ----------")
frase = "Todo Mundo Odeia o John"
nova_frase = frase.replace('o', 'x')
print(nova_frase)

# 7. find() - Retorna o índice da primeira ocorrência de um valor
# 8. index() - Retorna o índice da primeira ocorrência de um valor MAS gera um erro se não encontrar.
print("---------- find() e index() ----------")
frase = "Todo Mundo Odeia o John"
print(frase.find("Mundo"))
print(frase.index("M"))

# 9. count() - Conta o número de vezes que um valor aparece na string
print("---------- count() ----------")
frase = "Todo Mundo Odeia o John"
print(f"Quantidade de letra 'o': {frase.count('o')}")

# 10. isalpha() - Retorna True se todos os caracteres da string forem letras
frase = "TodoMundoOdeiaoJohn"

print(frase.isalpha())