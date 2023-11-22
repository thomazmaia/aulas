# 9. Crie um jogo para jogar com duas pessoas. O programa deve ter um número pré-definido onde só um jogador sabe e outro usuário deve adivinhar o número. Enquanto o número digitado não for igual ao número gerado, o programa continua pedindo para adivinhar.

numero_secreto = 10

numero_usuario = int(input("Digite um número: "))

while numero_usuario != numero_secreto:
    print("Número errado!")
    numero_usuario = int(input("Digite outro número: "))

print("Você acertou!")