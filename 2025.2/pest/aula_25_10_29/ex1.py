# Crie um programa para adicionar cidades em uma lista de cidades. Não permita que seja adicionada uma cidade existente.

cidades = []

for i in range (5):
    nome = input("Digite o nome de uma cidade: ")
    if nome not in cidades:
        cidades.append(nome)
        

print(cidades)