# Escreva um programa que crie um dicionário com 10 palavras e suas definições. O programa deve solicitar ao usuário cada chave e cada valor. Após adicionar as 10 palavras o usuário poderá pesquisar e exibir sua definição correspondente.

dicionario = {}

for i in range(2):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario[chave] = valor

print(dicionario)
chave = input("Qual chave você quer pesquisar o valor: ")

if chave in dicionario:
    print(dicionario[chave])
else:
    print("Chave inexistente")