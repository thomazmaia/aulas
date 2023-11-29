# Dicionário vazio
dicionario1 = {}
dicionario2 = dict()

# Criando dicionários com valores
lista = ['casa', 'rato', 'luz']
dicionario = {
    'casa' : 'house', 
    'rato' : 'mouse',
    'luz' : 'light'
    }

# Acessando elementos (pela chave - key)
print(dicionario['rato'])

for item in lista:
    print(dicionario[item])

# Alterando elementos
dicionario['casa'] = 'home'
print(dicionario['casa'])

dicionario['casa'] = ['house', 'home']
print(dicionario['casa'])

