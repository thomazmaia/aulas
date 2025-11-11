# Escreva uma função chamada concatenar_fatiar que aceite duas strings como entrada e retorne uma nova string que consiste nos três primeiros caracteres da primeira string concatenados com os três últimos caracteres da segunda string.

#Ex: concatenar_fatiar("Python", "Programming") deve retornar "Pyting”

def concatenar_fatiar(str1 : str, str2 : str):
    tres_primeiros = str1[0:3]
    tres_ultimos = str2[len(str2)-3:]
    nova_string = tres_primeiros + tres_ultimos
    return nova_string

print(concatenar_fatiar("Python", "Programming"))
print(concatenar_fatiar("abacaxi", "uva"))