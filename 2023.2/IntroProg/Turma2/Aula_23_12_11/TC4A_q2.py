senha = "ABC123"

tentativas = 1

while tentativas <= 3:
    nova_senha = input(f"Tentativa {tentativas}. Digite a senha: ")
    tentativas += 1
    if nova_senha != senha:
        print("Senha inválida.")
    else: 
        print("Cofre aberto.")
        break

if tentativas == 4:
    print("Cofre fechado.")