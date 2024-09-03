# Escreva um programa que crie um dicionário com 10 palavras e duas definições. O programa deve solicitar ao usuário cada chave e cada valor. Após adicionar as 10 palavras, o usuário poderá pesquisar e exibir sua definição correspondente.


dicionario = {}
for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor para '{chave}': ")
    dicionario[chave] = valor

print(dicionario)

while True:
    chave = input("Digite a chave: ")
    if chave in dicionario:
        print(dicionario[chave])
    else:
        print("Chave inexistente")