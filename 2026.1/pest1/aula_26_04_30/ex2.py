# Crie um código que leia uma string do usuário e verifique se essa string tem alguma vogal (A, E, I, O, U). Olhe apenas as minúsculas sem acento.

def verifica_vogal(str : str):
    flag = False
    for i in range(len(str)):
        if (str[i] == 'a') or (str[i] == 'e') or (str[i] == 'i') or (str[i] == 'o') or (str[i] == 'u'):
            flag = True

    if flag:
        print("tem vogal")
    else:
        print("Não tem vogal")

verifica_vogal("Abacaxi")
verifica_vogal("123")
