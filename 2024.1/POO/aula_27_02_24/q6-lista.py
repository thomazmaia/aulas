# 6. Faça um programa que leia o nome e o peso de várias pessoas guardando tudo em uma lista. No final mostre:
# (a) Quantas pessoas foram cadastradas
# (b) Uma listagem com as pessoas mais pesadas
# (c) Uma listagem com as pessoas mais leves

lista = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    aux = [nome, peso]
    lista.append(aux)
    sair = input("Sair? <s>")
    if sair in 'sS':
        break

qtd_de_pessoas = len(lista)
max = -99999
min = 999999

for i in range(qtd_de_pessoas):
    if lista[i][1] > max:
        max = lista[i][1]
        pesado = lista[i][0]
    if lista[i][1] < min:
        min = lista[i][1]
        leve = lista[i][0]

print(lista)
print(f"Mais pesado: {pesado} {max}kg")
print(f"Mais leve: {leve} {min}kg")
