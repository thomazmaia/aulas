# 1.  Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para
# inserir o nome de uma fruta e verifique se essa fruta está na lista.
# Exiba uma mensagem informando se a fruta está ou não na lista.

frutas = ["laranja", "limao", "abacaxi", "uva", "melancia"]

nova_fruta = input("Fruta: ")

flag = False
for fruta in frutas:
    if fruta == nova_fruta:
        flag = True

if flag:
    print("A fruta está na lista")
else:
    print("A fruta não está na lista")
