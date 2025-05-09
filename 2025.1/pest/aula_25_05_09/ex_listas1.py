# Exemplo: Dada a lista abaixo, imprima todos os seus elemento usando WHILE e, sem seguida, refaça usando FOR.

lista = [1, 2, "três", 4.5, 6.6, 10, -1, 0]

print("Usando WHILE:")
contador = 0
while contador <= 7:
    print(lista[contador])
    contador = contador + 1

print("Usando FOR:")
# usando for:
for contador in range(8):
    print(lista[contador])