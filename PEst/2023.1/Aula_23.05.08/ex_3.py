
notas = {}

while True:
    materia = input("Digite o nome da disciplina ou s para sair: ")
    if materia not in 'sS':
        notas[materia] = input(f"Digite a nota de {materia}: ")
    else:
        print(notas)
        break