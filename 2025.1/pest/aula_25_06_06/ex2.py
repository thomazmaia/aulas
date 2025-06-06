# 1 - Crie um programa para ler duas strings e mostre as duas invertidas.
# Ex: str1 = uva
#     str2 = limão
#     A saída deve ser "limãouva"

# str1 = input("Digite a primeira string: ")
# str2 = input("Digite a segunda string: ")
# res = str2 + str1
# print(res)

# 2 - Crie um programa para ler uma string e modifique o primeiro caractere da string para zero ("0").

string = input("Digite alguma coisa: ")
string = "0" + string[1:]
print(string)

# 3 - Leia duas strings e inverta o primeiro caractere delas. Ex: para "uva" e "limão" a saída deve ser "lva" e "uimão".

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

aux = str1[0]
str1 = str2[0] + str1[1:]
str2 = aux + str2[1:]
print(str1)
print(str2)