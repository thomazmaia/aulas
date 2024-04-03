# Métodos de strings
# ------------------
# Métodos = Função
#    Método com/sem retorno
#    Método com/sem parâmetros
# ------------------

# 1. upper() - Converte uma string para MAIÚSCULO
str = input("Digite alguma coisa: ")
res_up = str.upper()
print(f"Maiúsculo: {res_up}")

# 2. lower() - Converte uma string para MINÚSCULO
str = input("Digite alguma coisa: ")
res_lo = str.lower()
print(f"Minúsculo: {res_up}")

# 3. split() - Divide a string em substrings com base em um separador e retorna uma lista
frase = input("Digite uma frase: ").lower()
lista_frase = frase.split() # separador: espaço ' '
print(lista_frase)
lista_frase = frase.split('a') # separador: letra 'a'
print(lista_frase)

# 4. join() - Une elementos de uma lista em uma única string usando uma outra string como separador.
frase = input("Digite uma frase: ").upper()
palavras = frase.split()
print(palavras)
sep = ' '
nova_frase = sep.join(palavras)
print(nova_frase)

# 5. capitalize() - Converte o primeiro caractere para maiúsculo
nome = input("Digite seu nome: ").lower()
print(nome)
print(nome.capitalize())

# 6. replace() - Substitui um determinado trecho da string por outro.
nome = input("Nome: ").lower()
nome = nome.replace('a', '@')
print(nome)

# 7. find() - Retorna o índice da primeira ocorrência de um determinado valor
nome = input("Nome: ")
indice = nome.find('a')
print(nome)
print(indice)

# 8. index() - Semelhante ao 'find()' mas da erro se não encontrar
nome = input("Nome: ")
indice = nome.index('@')
print(nome)
print(indice)

# 9. count() - Conta o número de vezes que um determinado valor aparece na string
nome = input("Nome: ")
indice = nome.count('a')
print(nome)
print(indice)

# 10. islower() - Retorna True se uma string é minúscula.
str = input("Frase: ")

if str.islower():
    print("A string é minúscula")
else:
    print("A string NÃO é minúscula")