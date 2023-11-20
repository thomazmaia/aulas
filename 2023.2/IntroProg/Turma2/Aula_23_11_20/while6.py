senha_mestra = "python123"
tentativa = 0
saida = "acesso"

senha = input("Digite a senha: ")

while senha != senha_mestra:
    print("Senha inválida")
    tentativa = tentativa + 1
    print(f"Tentativa numero {tentativa}")
    if tentativa == 3:
        print("Bloqueado")
        saida = "bloqueio"
        break
    senha = input("Digite a senha: ")

if saida == "acesso":
    print("Acesso concedido!")