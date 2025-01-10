# CRIANDO LISTAS
# 1) Vazias
#  1.1) L = []
#  1.2) L = list()
# 2) Preenchidas
# L = ['uva', 'abacaxi', 'maçã', 'limão']

# A GRANDE DIFERENÇA ENTRE LISTAS E STRINGS
# --> Listas SÃO mutáveis <--



lista = ['P', 'i', 't', 'h', 'o', 'n']
print(lista)
lista[1] = "y"
print(lista)

# Ex: um aluno tem cinco notas e deseja calcular a média aritmética dele. Crie um código para fazer isso e mostrar a média.
notas = [6, 7, 5, 8, 9]

qtd_de_notas = len(notas)

soma = 0
for i in range(qtd_de_notas):
    soma = soma + notas[i]

media  = soma/qtd_de_notas
print(f"Média = {media}")