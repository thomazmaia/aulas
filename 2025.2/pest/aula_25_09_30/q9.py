from random import randint

def simulador_jogo_dados(num_rodadas : int):
    soma_jogador_1 = 0
    soma_jogador_2 = 0
    for i in range (num_rodadas):
        soma_jogador_1 = soma_jogador_1 + randint(1, 6) + randint(1, 6)
        soma_jogador_2 = soma_jogador_2 + randint(1, 6) + randint(1, 6)
        print(f"Soma do J1 após {i+1} rodadas: {soma_jogador_1}")
        print(f"Soma do J2 após {i+1} rodadas: {soma_jogador_2}")

    if soma_jogador_1 > soma_jogador_2:
        print("Ganhador: Jogador 1")
    elif soma_jogador_1 < soma_jogador_2:
        print("Ganhador: Jogador 2")
    else:
        print("Empate")


simulador_jogo_dados(10)