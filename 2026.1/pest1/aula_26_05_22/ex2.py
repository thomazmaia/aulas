# Crie um programa para ler cinco notas de um aluno (usuário) e calcule a sua média

def calcula_media(L : list):
    acumulador = 0
    for item in L:
        acumulador += item

    return (acumulador/len(L))


notas = [0, 0, 0, 0, 0]

i = 0
while i < 5:
    notas[i] = float(input(f"Digite uma nota {i+1}: "))
    i += 1

print(f"Notas: {notas}")

media = calcula_media(notas)
print(f"Média: {media}")