lista = [1, 2, 3, 1, 2, 1, 3, 3, 1, 2]
resultado = {}

for item in lista:
    if item in resultado.keys():
        resultado[item] += 1
    else:
        resultado[item] = 1

print(resultado)
