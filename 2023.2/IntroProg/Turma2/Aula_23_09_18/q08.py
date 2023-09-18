# Escreva um programa que peça ao usuário para digitar a sua altura em metros e,
# em seguida, imprima sua altura em centímetros e em pés. (1 metro = 100 centímetros,
# 1 pé = 0.3048 metros)

altura_m = float(input("Altura: "))

altura_cm = altura_m * 100

altura_pe = altura_m / 0.3048

print(f"{altura_m} equivalem a {altura_cm}cm e {altura_pe}pés")
