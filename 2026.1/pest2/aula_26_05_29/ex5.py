# ## Exercício 5 - Temperaturas da semana

# Crie um programa que:

# - Leia 7 temperaturas
# - Armazene as temperaturas em uma lista
# - Calcule a média da semana
# - Mostre quantos dias tiveram temperatura acima da média

def calc_media(lista : list):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma/len(lista)


L = [0, 0, 0, 0, 0, 0, 0]

for i in range(7):
    L[i] = int(input("Digite uma temperatura: "))

#L = [28.5, 29, 30, 29.5, 28, 28, 28]
print(L)

media = calc_media(L)

contador = 0
for item in L:
    if item >= media:
        contador += 1

print(f"{contador} dias com temperatura acima de {media}")