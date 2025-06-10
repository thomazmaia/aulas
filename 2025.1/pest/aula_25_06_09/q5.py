def concatenar_fatiar(s1 : str, s2 : str):
    nova_string = s1[0:3] + s2[-3:]
    return nova_string


print(concatenar_fatiar("Abacaxi", "Melancia"))