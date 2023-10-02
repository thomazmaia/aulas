# Crie uma lista de nomes de frutas. Em seguida, peça ao usuário para
# inserir o nome de uma fruta e verifique se essa fruta está na lista.
# Exiba uma mensagem informando se a fruta está ou não na lista.

L = ["limao", "laranja", "melancia", "uva", "pera", "maca"]

fruta = input("Fruta: ")

tamanho_da_lista = len(L)

flag = False

for indice in range(tamanho_da_lista):
    if fruta == L[indice]:
        flag = True

if flag == True:
    print("A fruta está na lista")
else:
    print("A fruta não está na lista")
