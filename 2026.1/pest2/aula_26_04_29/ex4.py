# Crie um programa para ler duas strings e informe o primeiro caractere de cada string.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"Primeiro caractere: {string1[0]}")
print(f"Primeiro caractere: {string2[0]}")

string1[0] = string2[0] # Strings são imutáveis