# Dada uma lista de nomes de frutas, crie um programa que peça ao usuário para digitar o nome de uma fruta para remover da lista. Certifique-se de que a fruta exista na lista antes de removê-la e imprima a lista resultante.

frutas = ['uva', 'banana', 'abacaxi', 'melancia']

nova_fruta = input("Digite o nome de uma fruta: ")

if nova_fruta in frutas:
    frutas.remove(nova_fruta)
else:
    print("A fruta não está na lista")

print(frutas)