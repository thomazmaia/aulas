# Crie uma função que receba duas strings e retorne uma nova string composta pelo primeiro caractere da primeira string e o último caractere da segunda string.
# Ex:
# cria_fruta("Uva", "Melancia") -> "Ua"

def cria_fruta(fruta1 : str, fruta2 : str):
    char1 = fruta1[0]
    char2 = fruta2[len(fruta2)-1]
    nova_string = char1 + char2
    return nova_string

print(cria_fruta("Banana", "Limao"))