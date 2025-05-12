# 1 - Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta está ou não na lista.

frutas = ['uva', 'abacaxi', 'morango', 'melancia']

fruta = input("Digite uma fruta: ")

for item in frutas:
    if(item == fruta):
        print("A fruta está na lista")