# Crie um programa que ajude os usuários a escolher o transporte adequado com base
# na distância que eles desejam percorrer. Solicite ao usuário que insira a
# distância em quilômetros e, em seguida, sugira o meio de transporte ideal com
# base na distância:
# "a pé" (até 1 km),
# "bicicleta" (até 10 km),
# "ônibus" (até 50 km) ou
# "carro" (acima de 50 km).

distancia = float(input("Distância (km): "))

if distancia <= 1:
    print("Vá a pé")
elif distancia <= 10:
    print("Vá de bicicleta")
elif distancia <= 50:
    print("Vá de ônibus")
else:
    print("Vá de carro")
