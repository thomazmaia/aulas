# 5. Escreva uma função chamada `concatenar_fatiar` que aceite duas strings como entrada e retorne uma nova string que consiste nos três primeiros caracteres da primeira string concatenados com os três últimos caracteres da segunda string.
# Ex: `concatenar_fatiar("Python", "Programming")`  deve retornar "Pyting”

def concatenar_fatiar(str1 : str, str2 : str):
    metade1 = str1[:3]
    metade2 = str2[-3:]
    return metade1 + metade2

print(concatenar_fatiar("Abacaxi", "Melancia"))