# Escreva um programa que crie um dicionário com 3 palavras e suas definições. O programa deve solicitar ao usuário cada chave e cada valor. Após adicionar as 3 palavras, o usuário poderá pesquisar e exibir sua definição correspondente.
# Adicione um função chamada "mostrar_dicionário(dict)" que deve receber o dicionário como argumento e mostrar seus pares chave-valor formatados dessa forma: [chave] : [valor]

def mostrar_dicionário(dicionario : dict):
    for k, v in dicionario.items():
        print(f"[{k}] - [{v}]")



dicionario = {}

for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor da chave {chave}: ")
    dicionario[chave] = valor

chave = input("Digite a chave que quer buscar: ")
print(dicionario[chave])

mostrar_dicionário(dicionario)