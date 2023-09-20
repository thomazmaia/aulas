# Escreva uma expressão que será utilizada para decidir
# se um aluno foi ou não aprovado. Para ser aprovado,
# todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias,
# e que a nota de cada uma está armazenada nas seguintes
# variáveis: Matérial, Matéria2 e Matéria3.

materia1 = float(input("Matéria 1: "))
materia2 = float(input("Matéria 2: "))
materia3 = float(input("Matéria 3: "))

media = (materia1 + materia2 + materia3) / 3
print(media)

res = media >= 7
print(res)
