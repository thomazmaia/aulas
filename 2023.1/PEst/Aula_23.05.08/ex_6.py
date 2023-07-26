jogadores = dict()

for i in range(5):
    nome = input("Digite o nome do jogador: ")
    pontos = int(input(f"Quantos pontos {nome} fez? "))
    jogadores[nome] = pontos

soma_de_pontos = 0
for _, valor in jogadores.items():
    soma_de_pontos += valor

pontuacao_media = soma_de_pontos / len(jogadores)

print(f"A pontuação média foi {pontuacao_media}")
