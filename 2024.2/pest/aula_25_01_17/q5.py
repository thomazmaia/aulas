# 5. Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta está ou não na lista.

frutas = ['uva','banana','abacaxi','laranja','limão']

nome_de_fruta = input("Digite o nome de uma fruta: ")

# # Maneira 1: while
# tamanho_da_lista = len(frutas)
# contador = 0
# while contador < tamanho_da_lista:
#     if frutas[contador] == nome_de_fruta:
#         print(f"A fruta {nome_de_fruta} está na lista")
#     contador = contador + 1

# Maneira 2: for
# tamanho_da_lista = len(frutas)
# for i in range(tamanho_da_lista):
#     if frutas[i] == nome_de_fruta:
#         print(f"A fruta {nome_de_fruta} está na lista")

# # Maneira 3: for
# for elemento in frutas:
#     if elemento == nome_de_fruta:
#         print(f"A fruta {nome_de_fruta} está na lista")

# Maneira 4: in
if nome_de_fruta in frutas:
    print(f"A fruta {nome_de_fruta} está na lista")
else:
    print(f"A fruta {nome_de_fruta} NÃO está na lista")