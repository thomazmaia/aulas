L = [4, 3.4, 'a', True, [1, 2, 3]]

# print(L[4]) # [1, 2, 3]
# print(L[4][1]) # 2

banco = [
    ['Bryan', [5, 6, 7, 8]],
    ['Leandro', [1, 2, 3, 4]],
    ['Rayssa', [9, 9, 9, 9]]
]

banco2 = []

# Adicionando BRYAN
aluno = []
aluno.append("Bryan")

notas = []
notas.append(5)
notas.append(6)
notas.append(7)
notas.append(8)
aluno.append(notas)

banco2.append(aluno)

# Adicionando LEANDRO
aluno = []
aluno.append("Leandro")

notas = []
notas.append(5)
notas.append(6)
notas.append(7)
notas.append(8)
aluno.append(notas)

banco2.append(aluno)

# Adicionando RAYSSA
aluno = []
aluno.append("Rayssa")

notas = []
notas.append(9)
notas.append(9)
notas.append(9)
notas.append(9)
aluno.append(notas)

banco2.append(aluno)

print(banco)
print(banco2)