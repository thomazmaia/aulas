# 1 - Crie um programa para ler uma string do usuário e imprima essa string caractere por caractere (um a um em cada linha.)

# str = input("Digite algo: ")

# for caractere in str:
#     print(caractere)

# 2 - Refaça o programa anterior mas imprima os caracteres ao contrário. Ex: ABACAXI deve imprimir IXACABA

str = input("Digite algo: ")

for i in range(len(str)-1, -1, -1):
    print(str[i])