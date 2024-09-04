# Como iterar em dicionários
dicionario = {
    "computador" : 40,
    "mouse" : 39,
    "mesa" : 20,
    "datashow" : 1,
    "ar condicionado" : 2
}

# 1. Como iterar pelas chaves (keys)
for item in dicionario.keys():
    print(item)

# 2. Como iterar pelos valores (values)
for item in dicionario.values():
    print(item)

# 3. Como iterar pelas chaves e valores (k, v)
for k, v in dicionario.items():
    print(f"Chave = {k}; Valor = {v}")