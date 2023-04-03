import random

def desenha_cabeca():
    print(" ----")
    print("|  |")
    print("|  o")
    print("|  ")
    print("|  ")
    print("|_  ")

def desenha_tronco():
    print(" ----")
    print("|  |")
    print("|  o")
    print("|  |")
    print("|  ")
    print("|_  ")

def desenha_braco_direito():
    print(" ----")
    print("|  |")
    print("|  o")
    print("|  |\ ")
    print("|  ")
    print("|_  ")

def desenha_braco_esquerdo():
    print(" ----")
    print("|  |")
    print("|  o")
    print("| /|\ ")
    print("|  ")
    print("|_  ")

def desenha_perna_direita():
    print(" ----")
    print("|  |")
    print("|  o")
    print("| /|\ ")
    print("|   \ ")
    print("|_  ")

def desenha_perna_esquerda():
    print(" ----")
    print("|  |")
    print("|  o")
    print("| /|\ ")
    print("| / \ ")
    print("|_  ")


opcao = ''

while opcao != 's':
    # Variáveis auxiliares
    lista_de_palpites = []
    num_erros = 0
    num_acertos = 0

    # Configuração da palavra secreta
    lista_de_palavras = ['LIMAO', 'LARANJA', 'ABACAXI', 'MACA']
    palavra_secreta = random.choice(lista_de_palavras)
    tamanho_da_palavra_secreta = len(palavra_secreta)

    # Início do jogo
    print("------- Jogo da Forca -------")
    print(f"A palavra tem {tamanho_da_palavra_secreta} letras.")

    # Laço principal
    while num_erros < 6 and num_acertos != tamanho_da_palavra_secreta:
        # Mostrar as letras da palavra secreta
        for letra in palavra_secreta:
            if letra in lista_de_palpites:
                print(letra, end=' ')    
            else:
                print("_", end=' ')
        print()    

        # Pegar um palpite (letra)
        palpite = input("Digite uma letra: ").upper()

        # Verifica se palpite já foi dado
        if palpite in lista_de_palpites:
            print(f"A letra {palpite} já foi utilizada")
        else:
            lista_de_palpites.append(palpite)
            # Verifica se o palpite está certo ou errado
            if palpite in palavra_secreta:
                print("Acertou!!")
                num_acertos += palavra_secreta.count(palpite)
            else:
                print("Errou!!")
                num_erros += 1
                if num_erros == 1:
                    desenha_cabeca()
                elif num_erros == 2:
                    desenha_tronco()
                elif num_erros == 3:
                    desenha_braco_direito()
                elif num_erros == 4:
                    desenha_braco_esquerdo()
                elif num_erros == 5:
                    desenha_perna_direita()
                elif num_erros == 6:
                    desenha_perna_esquerda()
    
    # Verificar se ganhou ou perdeu
    if num_erros == 6:
        print("Você perdeu.")
    elif num_acertos == tamanho_da_palavra_secreta:
        print("Você ganhou.")
    
    # Opção para jogar novamente ou sair
    opcao = input("Digite `s` para sair ou qualquer coisa para jogar novamente.").lower()
