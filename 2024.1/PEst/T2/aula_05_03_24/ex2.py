# 2. Crie uma função que receba 4 parâmetros: dois nomes de pessoas e as suas respectivas idades. Verifique quem é o mais velho e escreva o nome do mais velho. Utilize parâmetros posicionais nomeados.

def verifica_mais_velho(nome1 : str, nome2 : str, idade1 : int, idade2 : int):
    if idade1 > idade2:
        print(f"Mais velho é o(a) {nome1}")
    else:
        print(f"Mais velho é o(a) {nome2}")



nome1 = input("Nome: ")
idade1 = int(input("Idade: "))
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))

verifica_mais_velho(nome1=nome1, nome2=nome2, idade1=idade1, idade2=idade2)