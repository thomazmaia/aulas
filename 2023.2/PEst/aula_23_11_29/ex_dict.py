dict = {
    'um' : 'one',
    1 : 'um',
    '1' : 1,
    'um' : 1,
    1 : 1
}

# Tamanho do dicionário
print(len(dict))

# Percorrendo os elementos do dicionário
for chave, valor in dict.items():
    print(f"Elemento {chave} : {valor}")
# Outra forma (não indicado)
for item in dict:
    print(f"Elemento {item} : {dict[item]}")

# Adicionar elementos
dict['chave'] = "valor qualquer"
print(dict)

# Remover elementos
del dict['chave']
print(dict)