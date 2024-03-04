# 2. Crie uma função que receba 4 parâmetros: dois nomes de pessoas e as suas respectivas idades. Verifique em é o mais velho e escreva o nome do mais velho. Utilize parâmetros posicionais nomeados.

def verifica_idade(nome1 : str, nome2 : str, idade1 : int, idade2 : int):
    if idade1 > idade2:
        print(f"Mais velho: {nome1}")
    else:
        print(f"Mais velho: {nome2}")


nome1 = input("Nome: ")
idade1 = input("Idade: ")
nome2 = input("Nome: ")
idade2 = input("Idade: ")

verifica_idade(nome1 = nome1, idade1 = idade1, nome2 = nome2, idade2 = idade2)