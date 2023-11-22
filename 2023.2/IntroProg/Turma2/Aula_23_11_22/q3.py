# 3. Modifique o exercício anterior para aceitar números positivos e negativos.

numero = int(input("Número: "))

if numero > 0:
    # Numero positivo
    while numero >= 0:
        print(numero)
        numero -= 1     # numero = numero - 1
else:
    # Numero negativo
    while numero <= 0:
        print(numero)
        numero += 1     # numero = numero + 1