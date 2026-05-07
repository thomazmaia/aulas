# Crie uma função que receba duas strings e retorne uma nova string formada pelo primeiro caractere da segunda string e o último caractere da primeira string.
# Ex: "Abacaxi" e "Uva" -> "Ui"

def nova_string(string1 : str, string2 : str):
    char1 = string2[0]
    char2 = string1[len(string1)-1]
    return char1 + char2


print(nova_string("Limão", "Ata"))