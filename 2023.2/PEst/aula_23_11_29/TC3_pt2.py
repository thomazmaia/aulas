lista = [10, 3, 5, 0, 3, 3, 7, 8, 2, 9]

lista.sort()
min = lista[0]
max = lista[-1]

print(lista)
print(f"min = {min}, max = {max}")

soma = 0
for item in lista:
    soma += item
print(f"Soma = {soma}")

nova_lista = []

for item in lista:
    if item % 2 != 0:
        nova_lista.append(item)

lista = nova_lista
print(lista)
print(nova_lista)