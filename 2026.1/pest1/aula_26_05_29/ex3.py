# Escreva um programa que peça ao usuário para inserir nomes de frutas e armazene-os em uma lista até que apareça a fruta 'abacaxi' ou o usuário digite 0 para sair. Ao final, mostre a lista de frutas.

frutas = []

while True:
    nome = input("Digite a fruta: ")
    if nome == "0":
        break
    elif nome == "abacaxi":
        frutas.append(nome) 
        break
    
    frutas.append(nome) 

print(frutas)