# 3. Crie uma lista de frutas quaisquer. Em seguida, peça ao usuário para inserir o nome de uma fruta e verifique se essa fruta está na lista. Exiba uma mensagem informando se a fruta está ou não.

frutas = ["maça", "banana", "laranja", "uva"]

nova_fruta = input("Digite o nome da fruta: ")

if nova_fruta in frutas:
    print("A fruta está na lista")
else:
    print("A fruta NÃO está na lista")

# flag = False
# for i in range(len(frutas)):
#     if frutas[i] == nova_fruta:
#         flag = True

# if flag == True:
#     print("A fruta está na lista")
# else:
#     print("A fruta não está na lista")