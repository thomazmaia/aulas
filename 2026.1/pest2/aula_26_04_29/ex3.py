# Crie um código para ler duas strings do usuário e informa qual das duas é maior (usando funções).

def verifica_maior(str1 : str, str2 : str):
    tamanho1 = len(str1)
    tamanho2 = len(str2)
    if tamanho1 > tamanho2:
        print(f"String 1 ({str1}) é maior")
    elif tamanho2 > tamanho1:
        print(f"String 2 ({str2}) é maior")
    else:
        print("O tamanho das strings é o mesmo")

string_do_usuario1 = input("Digite a string 1: ")
string_do_usuario2 = input("Digite a string 2: ")

verifica_maior(string_do_usuario1, string_do_usuario2)