# Crie um código para ler duas strings do usuário e informe qual das duas é maior (usando funções).

def verifica_maior(str1 : str, str2 : str):
    if len(str1) == len(str2):
        print("Tem o mesmo tamanho")
    elif len(str1) > len(str2):
        print(f"{str1} é maior que {str2}")
    else:
        print(f"{str2} é maior que {str1}")

string1 = input("String 1: ")
string2 = input("String 2: ")
verifica_maior(string1, string2)