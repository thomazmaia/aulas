# Crie uma função que receba duas string e retorne uma nova string composta pela segunda string invertida e a primeira normal.
# Ex: 'Abacaxi' e 'Uva' -> 'avUAbacaxi'

def duas_strings(str1 : str, str2 : str):
    invertida = str2[::-1]
    nova_string = invertida + str1
    return nova_string

print(duas_strings("Melancia", "Limão"))