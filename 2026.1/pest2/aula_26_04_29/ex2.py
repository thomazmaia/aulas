# Crie um código que leia uma string do usuário e verifique se essa string tem alguma vogal (A, E, I, O, U).

def verifica_vogal(string : str):
    tamanho = len(string)
    for i in range(tamanho):
        if string[i] == 'A' or string[i] == 'a' or string[i] == 'E' or string[i] == 'e' or string[i] == 'I' or string[i] == 'i' or string[i] == 'O' or string[i] == 'o' or string[i] == 'U' or string[i] == 'u':
            return True

    return False


string_do_usuario = input("Digite alguma coisa: ")

if verifica_vogal(string_do_usuario):
    print("Tem vogal")
else:
    print("Não tem vogal")