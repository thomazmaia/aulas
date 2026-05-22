# Dada a lista de notas do John, calcule a sua média em PEST:

notas = [10, 6, 8, 4, 7.5, 2]

acumulador = 0
for nota in notas:
    acumulador += nota

media = acumulador / len(notas)

print(media)