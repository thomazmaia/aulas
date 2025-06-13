# Escreva um programa que crie um dicionário com 5 palavras e suas definições. O programa deve solicitar ao usuário cada chave (palavra) e cada valor (definição). Após adicionar as 5 chaves/definições o usuário poderá pesquisar uma palavra e exibir a definição correspondente.

dicionario = dict() # {}

for i in range(3):
    chave = input(f"Digite a palavra chave {i+1}: ").lower()
    valor = input(f"Digite a definição para {chave}: ").lower()
    dicionario[chave] = valor

while True:
    chave = input("Digite a chave ou zero para sair: ").lower()
    if chave == "0" or chave == "zero":
        break
    else:
        # Verificar se a chave existe antes:
        if chave in dicionario:
            print(dicionario[chave])
        else:
            print("Chave inexistente")