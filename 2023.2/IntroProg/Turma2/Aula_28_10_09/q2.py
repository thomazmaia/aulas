# Crie um programa para verificar se um aluno foi aprovado em uma disciplina com base em sua nota. Solicite ao usuário que insira a nota do aluno (em uma escala de 0 a 10) e, em seguida, informe se o aluno foi aprovado (nota maior ou igual a 6) ou reprovado (nota menor do que 6).

nota = float(input("Nota: "))


if (nota >= 0) and (nota <= 10):
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Nota inválida")
