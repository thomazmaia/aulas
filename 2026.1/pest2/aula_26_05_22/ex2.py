# Crie um programa para ler cinco notas de um aluno (usuário/input) e calcule a sua média

def calcula_media(L : list):
    acc = 0
    for item in L:
        acc += item
    return acc/len(L)


notas = [0, 0, 0, 0, 0]

for i in range(5):
    notas[i] = float(input(f"Digite a nota {i+1}: "))

print(notas)
media = calcula_media(notas)
print(f"A média foi de {media}")