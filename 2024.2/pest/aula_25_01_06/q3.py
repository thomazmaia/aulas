def reverter(entrada : str):
    invertida = entrada[-1: -len(entrada)-1 :-1]
    return invertida

print(reverter("Abacaxi"))