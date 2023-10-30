# Peça ao usuário para inserir sua idade e, com base na idade fornecida, informe se a pessoa é:
# uma criança (0-12 anos),
# adolescente (13-19 anos),
# adulto (20-59 anos) ou
# idoso (60 anos ou mais).

idade = int(input("Idade: "))

if (idade >= 0) and (idade <= 12):
    print("Criança")
elif (idade >= 13) and (idade <= 19):
    print("Adolescente")
elif (idade >= 20) and (idade <= 59):
    print("Adulto")
elif idade >= 60:
    print("Idoso")
