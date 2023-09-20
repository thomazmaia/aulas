# Tempo de Viagem: Pergunte ao usuário a distância em
# quilômetros que eles pretendem viajar e a velocidade
# média em km/h. Calcule o tempo estimado de viagem e
# imprima-o.

distancia = int(input("Distância: "))
velocidade_media = int(input("Velocidade média: "))

tempo = distancia / velocidade_media

print(f"{distancia}km a {velocidade_media}km/h demora {tempo} horas.")
