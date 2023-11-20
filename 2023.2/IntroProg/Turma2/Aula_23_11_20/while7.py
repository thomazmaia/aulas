# Leia 5 notas de um aluno e calcule a média.

contador = 1
acumulador = 0
quantidade_de_notas = 50

while contador <= quantidade_de_notas:
    N = float((input(f"Digite a nota {contador}: ")))
    acumulador = acumulador + N
    contador = contador + 1

media = acumulador/quantidade_de_notas

print(media)
