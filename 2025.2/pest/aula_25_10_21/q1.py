# Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta está ou não na lista.

lista_de_frutas = ['uva', 'maça', 'banana', 'laranja']

print(f"A lista tem {len(lista_de_frutas)} frutas")


nome = input("Digite o nome da fruta: ")
flag = False

for i in range(len(lista_de_frutas)):
    if nome == lista_de_frutas[i]:
        flag = True

if flag == True:
    print("A fruta está na lista")
else:
    print("A fruta não está na lista")