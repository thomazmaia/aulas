def saudacao(nome : str = "Anônimo", idade : int = 0):
    print(f"Olá {nome}, você tem {idade} anos.")


# Programa principal
nome_da_pessoa = input("Digite o nome da pessoa: ")
idade_da_pessoa = int(input("Digite a idade da pessoa: "))

# Argumento/parâmetro nomeado
saudacao(idade=idade_da_pessoa)