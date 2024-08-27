lista_de_alunos = [
    ['José', 15, [6, 7, 8]],
    ['João', 16, [7, 8, 8]],
    ['Maria', 16,[7, 7, 7]]
]

print(lista_de_alunos[0]) # ['José', 15, [6, 7, 8]]
print(lista_de_alunos[0][2]) # [6, 7, 8]
notas_do_aluno = lista_de_alunos[0][2] # [6, 7, 8]
soma = 0
for nota in notas_do_aluno:
    soma += nota
media = soma/3
