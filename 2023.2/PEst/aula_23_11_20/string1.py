# Métodos de strings
#####################################################
# # 1. upper() e lower()
# texto = input("Texto: ")
# maiusculas = texto.upper()
# minusculas = texto.lower()
# print(f"Em maiusculas: {maiusculas}")
# print(f"Em minusculas: {minusculas}")
#####################################################
# # 2. split()
# texto = "Isso é um exemplo de texto!"
# lista = texto.split()
# for item in lista:
#     print(item)
#####################################################
# # 3. join()
# texto = "Isso é um exemplo de texto!"
# lista = texto.split()
#
# print(lista)
#
# novo_texto = ' '.join(lista)
# print(novo_texto)
#####################################################
# # 4. capitalize()
# frase = input("Frase: ")
# #frase = frase.capitalize()
# slice1 = frase[0].upper()
# slice2 = frase[1::].lower()
# nova_frase = slice1+slice2
# print(nova_frase)
#####################################################
# # 5. replace()
# frase = input("Digite uma frase: ")
#
# nova_frase = frase.replace(' de ', ' X ')
# print(nova_frase)
#####################################################
# # 6. find() e index()
# string = "isso é um exemplo!"
# print(string.find('!'))  # <--- USA ESSE :)
# print(string.index('!'))
#####################################################
# # 7. count()
# string = "isso é exumplo um!"

# contagem = string.count('um')

# print(contagem)