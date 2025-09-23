# Defina uma função chamada cumprimentar que aceita dois parâmetros nomeados: nome e saudacao. Se o parâmetro saudacao não for fornecido, use a saudação "Olá". A função deve imprimir o cumprimento personalizado.


def cumprimentar(nome : str, saudacao : str = "Olá"):
    print(f"{saudacao}, {nome}")


cumprimentar("Maria", "Bem vinda")
cumprimentar("João", "Tchau")
cumprimentar("Xikin") # Função com parâmetros com valores padrão