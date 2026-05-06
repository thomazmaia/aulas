# Fatiamento (slicing) de strings
# Fatiar uma string é fazer uma cópia de uma parte da string. Essa cópia é feita através de um intervalo definido entre colchetes.
# Ex:
# nome = "Francisco"
# print(nome[0:4]) -> "Fran"

nome = "Francisco"
#       012345678

print(nome[0:4])
print(nome[4:9])
print(nome[4:len(nome)])
print(nome[4:])

# Exemplos de fatiamento:
# [inicio : fim : passo]
nome = "Francisco"

print(f"Inicio ao fim: {nome[0:]}")
print(f"Inicio ao fim: {nome[ : ]}")
print(f"Inicio ao fim: {nome[ : : ]}")
print(f"Inicio ao fim: {nome[0:9:1]}")
print(f"Intervalo: {nome[3:7]}")
print(f"Intervalo com passo: {nome[1:7:2]}")
print(f"Intervalo com passo: {nome[3:7:3]}")
print(f"Intervalo com passo negativo: {nome[ : :-1]}")