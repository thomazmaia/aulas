cadastro = [
    ['Davi', [9.1, 9.2, 9.3]],
    ['Gaspar', [5.1, 5.2, 5.3]],
    ['Isabelly', [9.8, 9.9, 10]]
]

banco = []

# Adicionando o DAVI
notas = []
notas.append(9.1)
notas.append(9.2)
notas.append(9.3)

aluno = []
aluno.append('Davi')
aluno.append(notas)

banco.append(aluno)

# Adicionando o GASPAR
notas = []
notas.append(5.1)
notas.append(5.2)
notas.append(5.3)

aluno = []
aluno.append('Gaspar')
aluno.append(notas)

banco.append(aluno)

# Adicionando a ISABELLY
notas = []
notas.append(9.8)
notas.append(9.9)
notas.append(10)

aluno = []
aluno.append("Isabelly")
aluno.append(notas)

banco.append(aluno)

print(cadastro)
print(banco)

#print(cadastro[1][0]) # Gaspar

#print(cadastro[2][1][2]) # 10