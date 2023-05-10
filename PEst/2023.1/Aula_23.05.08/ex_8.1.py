lista = [1, 2, 3, 1, 2, 1, 3, 3, 1, 2]
resultado = {}

for item in lista:
    resultado[item] = lista.count(item)

print(resultado)
