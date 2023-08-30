def saudacao(sexo, nome_da_pessoa):
    if sexo == "m":
        print(f"Seja bem vindo, {nome_da_pessoa}")
    elif sexo == "f":
        print(f"Seja bem vinda, {nome_da_pessoa}")


saudacao(nome_da_pessoa="João", sexo="m")
saudacao(nome_da_pessoa="Maria", sexo="X")
saudacao(sexo="m", nome_da_pessoa="José")
