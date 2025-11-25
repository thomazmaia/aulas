# 1. Crie e mostre um dicionário com as seguintes chaves e valores:
# ---------
# Nome : João da Silva
# Idade : 30
# Cidade : Maranguape
# ---------
dicionario = {
    "Nome" : "João da Silva",
    "Idade" : 30,
    "Cidade" : "Maranguape"
}

print(dicionario)

# 2. Crie um dicionário que represente uma lista de compras. As chaves devem ser os nomes dos produtos e os valores devem ser as quantidades desses produtos a serem comprados.
lista_de_compras = {}
lista_de_compras["arroz"] = 11
lista_de_compras["feijão"] = 7
lista_de_compras["macarrão"] = 5
lista_de_compras["farinha"] = 20
print(lista_de_compras)

# 3. Use um loop for para ITERAR sobre o dicionário da lista de compras da questão anterior e mostre todos os itens, um a um.
for k, v in lista_de_compras.items():
    print(f"[{k}] - {v} unid.")