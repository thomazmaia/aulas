numero_secreto = 42

tentativas = 1
while tentativas <= 5:
    palpite = int(input(f"Tentativa {tentativas}: "))
    if palpite > numero_secreto:
        print("Digite um número menor!")
    if palpite < numero_secreto:
        print("Digite um número maior")
    if palpite == numero_secreto:
        print("Acertou")
        break
    tentativas += 1

if tentativas > 5:
    print("Você perdeu!")