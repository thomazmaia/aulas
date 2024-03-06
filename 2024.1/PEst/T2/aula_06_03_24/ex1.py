def saudacao(nome):
    print(f"Olá {nome}")

def pega_nome():
    nome = input("Digite o seu nome: ")
    return nome


resp = pega_nome()
saudacao(resp)