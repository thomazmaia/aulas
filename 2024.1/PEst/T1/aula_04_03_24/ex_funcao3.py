def saudacao(nome : str, idade : int):
    print(f"Olá {nome}, você tem {idade} anos.")



# Programa principal
pessoa = input("Digite o nome da pessoa: ")
idade_da_pessoa = int(input("Digite a idade da pessoa: "))
saudacao(pessoa, idade_da_pessoa)
# Parâmetros posicionais
saudacao(20, "Fulano")
