def saudacao(nome_da_pessoa, sexo="m", local="IFCE"):
    if sexo == "m":
        print(f"Seja bem vindo, {nome_da_pessoa}, ao {local}")
    elif sexo == "f":
        print(f"Seja bem vinda, {nome_da_pessoa}, ao {local}")


saudacao("João")
saudacao("Maria", "f", "MPE")
