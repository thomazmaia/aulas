# Leia 5 notas do usuário, coloque-as numa lista e calcule
# a média dessas notas.
# OBS: Só calcule a média depois que as notas estiverem na lista!

notas = [0, 0, 0, 0, 0]

for i in range(5):
    notas[i] = input(f"Digite a nota {i+1}: ")

print(notas)