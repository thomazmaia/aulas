def saudacao(sexo, nome_da_pessoa):
    if sexo == "m":
        print(f"Seja bem vindo, {nome_da_pessoa}")
    elif sexo == "f":
        print(f"Seja bem vinda, {nome_da_pessoa}")


saudacao("João", "m")
saudacao("Maria", "X")
saudacao("m", "José")
