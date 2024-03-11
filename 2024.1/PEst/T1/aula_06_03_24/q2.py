# Defina uma função chamada cumprimentar que aceita dois parâmetros nomeados: nome e saudacao. Se o parâmetro saudacao não for fornecido, use a saudação "Olá". A função deve imprimir o cumprimento personalizado.

def cumprimentar(nome : str, saudacao : str = "Olá"):
    print(f"{saudacao}, {nome}")

nome = input("Nome: ")
saud = input("Saudação: ")

if saud == "":
    cumprimentar(nome)
else:
    cumprimentar(nome, saud)

cumprimentar("Zezin", "Aloha")
cumprimentar("Xikin", "Oi")
cumprimentar("Maria")