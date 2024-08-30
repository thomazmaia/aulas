# 1. Crie uma lista de pontuações de jogadores em um jogo. Use o método sort() para classificar as pontuações em ordem decrescente e, em seguida, use o método index() para encontrar a posição de um jogador específico no ranking.

pontuacoes = [10, 20, 25, 5, 15, 2, 50]

pontuacoes.sort(reverse=True)

posicao = pontuacoes.index(25) + 1
print(pontuacoes)
print(f"O jogador cuja pontuação foi 25 está na posição {posicao}")