# Crie uma função que receba o nome e a idade de uma pessoa e escreva quantos anos ela terá no ano que vem.
# Ex: (nome = maria; idade = 17)
#   "Maria, ano que vem você terá 18 anos"

def calcula_idade(nome, idade):
    aux = idade + 1
    print(f"{nome}, ano que vem você terá {aux} anos")

calcula_idade("Maria", 17)