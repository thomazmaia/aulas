# Altere o exercício anterior para adicionar as funções de
# adicionar um item (par chave-valor), remover um item e 
# limpar o dicionário.

dicionario = dict()

for i in range(2):
    chave = input(f"Digite a {i+1}a chave: ")
    valor = input(f"Digite o {i+1}o valor: ")
    adicionar_item(chave, valor)
    dicionario[chave] = valor

while True:
    chave_pesquisa = input("Digite a chave: ")
    print(dicionario[chave_pesquisa])