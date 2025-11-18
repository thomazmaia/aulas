# Escreva um programa que crie um dicionário com 10 palavras e suas definições. O programa deve solicitar ao usuário cada chave (palavra) e cada valor (definição). Após adicionar as 10 palavras o usuário poderá pesquisar uma palavra e exibir sua definição correspondente.

dicio = dict()

for i in range(3):
    palavra = input("Digite uma palavra: ")
    definicao = input("digite a definição: ")
    dicio[palavra] = definicao
    
print(dicio)