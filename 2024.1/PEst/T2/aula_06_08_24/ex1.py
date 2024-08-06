# 1. Leia 5 notas do usuário, coloque-as numa lista e, só depois, calcule a média desse usuário.

notas = [0, 0, 0, 0, 0]

for i in range(5):
    notas[i] = float(input(f"Digite a {i+1}a nota: "))

print(notas)

soma = 0
for elemento in notas:
    soma += elemento

media = soma/len(notas)
print(media)