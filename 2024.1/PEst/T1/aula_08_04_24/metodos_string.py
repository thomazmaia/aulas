# Métodos de strings
# ------------------
# Métodos = funções
#   Com/sem retorno
#   Com/sem parâmetros
# ------------------

# 1. capitalize() - Retorna a string com o primeiro caractere em caixa alta
nome = input("Digite seu nome: ")
print(nome)
print(nome.capitalize())

# 2. lower() - Converte a string para minúsculo
nome = input("Digite seu nome: ")
print(nome)
print(nome.lower())

# 3. upper() - Converte a string para MAIÚSCULO
nome = input("Digite seu nome: ").upper()
print(nome)
print(nome.upper())

# 4. split() - Divide a string com base em um separador e retorna uma lista
frase = "Hoje é um bom dia"
lista_frase = frase.split() # separador: espaço ' '
print(lista_frase)
lista_frase = frase.split('m') # separador: 'm'
print(lista_frase)

# 5. join() - Une elementos de uma lista usando uma string como "separador"
frase = "Hoje é um bom dia"
lista_frase = frase.split('m')
print(lista_frase)
palavra = "#"
print(palavra.join(lista_frase))

# 6. replace() - Substitui um determinado trecho da string por outro
nome = input("Digite seu nome: ").upper()
nome = nome.replace('ABACAXI', 'MELANCIA')
nome = nome.replace('A', '4')
nome = nome.replace('E', '3')
nome = nome.replace('I', '1')
nome = nome.replace('O', '0')
print(nome)

# 7. find() - Retorna o índice da primeira ocorrência de um determinado valor
frase = "Hoje é um bom dia"
print(frase.find('m')) # 8
print(frase.find('x')) # -1

# 8. index() - Mesma coisa do find() mas da erro se não existir.
frase = "Hoje é um bom dia"
print(frase.index('m')) # 8
print(frase.index('x')) # ERRO!

# 9. count() - Conta o número de ocorrências de um determinado valor numa string
frase = "Hoje é um bom dia"
print(frase.count('m')) # 2
print(frase.count('M')) # 0

# 10. islowe() - Retorna True se a string for minúscula
frase = "hoje"
if frase.islower() == True:
    print("Tudo minúsculo")
else:
    print("NEM Tudo é minúsculo")