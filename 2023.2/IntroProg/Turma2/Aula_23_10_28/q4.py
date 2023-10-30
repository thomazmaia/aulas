# Desenvolva um programa para calcular o custo do envio de um pacote com base no
# peso e na distância. Solicite ao usuário que insira o peso do pacote
# (em quilogramas) e a distância a ser percorrida (em quilômetros).
# Calcule o custo do envio usando a seguinte regra: se o peso for menor ou igual
# a 10 kg e a distância for menor ou igual a 50 km, o custo é de R$ 20;
# caso contrário, o custo é de R$ 30.

peso = float(input("Peso (em kg): "))
distancia = float(input("Distancia (em km): "))

if peso <= 10 and distancia <= 50:
    print("Envio: R$ 20")
else:
    print("Envio: R$ 30")
