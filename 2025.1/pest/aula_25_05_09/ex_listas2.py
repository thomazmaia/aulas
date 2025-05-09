# Dada a lista de notas abaixo, inicialmente zerada, leia as notas de um aluno e modifique os valores dessa lista.
# Ex: notas = [0, 0, 0, 0]
#     nota 1 do aluno: 10
#     nota 2 do aluno: 8.8
#     nota 3 do aluno: 7.5
#     nota 4 do aluno: 9
#     notas = [10, 8.8, 7.5, 9]


notas = [0, 0, 0, 0, 0, 0, 0 , 0]
tamanho_da_lista = 8

for i in range(tamanho_da_lista):
    notas[i] = float(input(f"Digite a nota {i+1} do aluno: "))

print(notas)

# Calculando a média das notas do aluno:
soma = 0
for i in range(tamanho_da_lista):
    soma = soma + notas[i]
media = soma/tamanho_da_lista

print(f"A média desse aluno foi: {media}")