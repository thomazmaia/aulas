# 1. Crie uma lista de frutas quaisquer. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta está ou não.


lista_de_frutas = ['laranja', 'banana', 'abacaxi', 'mamão']

fruta = input("Digite a fruta: ")

if fruta in lista_de_frutas:
    print("Já está na lista de frutas.")
else:
    print(f"{fruta} não está na lista de frutas.")