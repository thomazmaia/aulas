def calcular_media(lista):
    soma = 0
    for item in lista:
        soma += item
    return(soma/len(lista))


lista = [1, 2, 3]
print(calcular_media(lista))

def calcular_min_max(lista):
    lista.sort()
    return [lista[0], lista[-1]]

lista = [1, 2, 3]
print(calcular_min_max(lista))

def inverter_string(string):
    return string[::-1]

print(inverter_string("abacaxi"))