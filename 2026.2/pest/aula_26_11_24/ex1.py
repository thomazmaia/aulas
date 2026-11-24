notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tamanho = len(notas)

for i in range(tamanho):
    notas[i] = int(input(f"Digite a sua nota {i+1}: "))

print(notas)