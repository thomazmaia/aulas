# FATIAMENTO DE LISTAS (SLICING):
# Podemos acessar uma parte da lista utilizando o fatiamento (slicing). O fatiamento é feito utilizando dois pontos (:) para indicar o início e o fim do intervalo que desejamos acessar.
# lista[inicio:fim:passo]
#
# Exemplo de fatiamento de listas
lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print(lista[0:3])  # Acessa os elementos do índice 0 ao 2 (não inclui o índice 3)
print(lista[2:4]) # [3, 4]
print(lista[3]) # 4

print(lista[5:10]) # letras
print(lista[5:]) # letras também
print(lista[0:5]) # números
print(lista[:5]) # números também
print(lista[:]) # lista inteira

lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print(lista[::2]) # inicia do primeiro, vai até o fim, pulando de dois em dois
print(lista[3:8:3]) # [4, b]

print(lista[5]) # 'a'
print(lista[-5]) # 'a'