string = 'STRING é uma LISTA de caracteres'

# Indexando elementos na string
primeira_letra = string[0]
letra_qualquer = string[6]
ultima_letra = string[-1]

# Fatiando a string
fatia = string[4:12]

# Percorrendo os elementos
for letra in fatia:
    print(letra)

# Strings são IMUTÁVEIS depois de criadas
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")

# Concatenação
outra = nome + ' ' + sobrenome
print(outra)

# Repetição
string = "olê "
print(string*5)

# Verificação se existe um caractere dentro da string
while True:
    op = input("")
    if op in 'sS':
        break

# Tamaho da string
print(len(string))


