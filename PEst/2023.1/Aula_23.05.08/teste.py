d = {'Joao' : 3, 'Artur' : 2, 'Julia' : 1, 'Julia' : 10}

# Acessando valor pela chave
for chave in d.keys():
    print(f"{chave} : {d[chave]}")

# Acessando chave e valor ao mesmo tempo:
for chave, valor in d.items():
    print(f"{chave} : {valor}")