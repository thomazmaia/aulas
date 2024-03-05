# Argumentos/parâmetros nomeados

def saudacao(nome : str, idade : int):
    print(f"Olá {nome} de {idade} anos")


saudacao(nome="Maria", idade=20)
saudacao(idade=20, nome="Maria")