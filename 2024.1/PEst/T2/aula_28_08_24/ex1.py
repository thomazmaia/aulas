# 1. Crie uma lista de pontuações de jogadores em um jogo. Use o método sort() para classificar as pontuações em ordem decrescente e, em seguida, use o método index() para encontrar a posição de um jogador específico no ranking.

pontuacoes = [20, 30, 40, 15, 35]

pontuacoes.sort(reverse=True)

posicao_jogador = pontuacoes.index(30)+1

print(pontuacoes)
print(f"O jogador cuja pontuação foi 30 está na posição {posicao_jogador}")