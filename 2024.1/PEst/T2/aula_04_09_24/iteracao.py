# Como iterar por dicionários
dicionario = {
    'computador' : 40,
    'datashow' : 1,
    'teclado' : 40,
    'mouse' : 40,
    'ar condicionado' : 2
}

# 1. Iterar por chaves (keys)
for chave in dicionario.keys():
    print(chave)

# 2. Iterar por valores (values)
for valor in dicionario.values():
    print(valor)

# 3. Iterar por chave e valor (key e value)
for chave, valor in dicionario.items():
    print(f"{chave} - {valor}")