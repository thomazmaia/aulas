# 4 - Crie um programa que peça três informações:
# - Nome
# - Idade
# - Curso

# Depois, mostre os dados informados, cada um em uma linha.

# Exemplo:
#     Nome: Ana
#     Idade: 18
#     Curso: Informática

#     Dados cadastrados:
#     Nome: Ana
#     Idade: 18
#     Curso: Informática


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite seu curso: ")

print("Dados cadastrados:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Curso: {curso}")