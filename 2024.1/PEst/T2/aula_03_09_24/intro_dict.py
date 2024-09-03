# 1. Como criar dicionários
dicionario = {}     # dicionário vazio
dicionario = dict() # dicionário vazio

dicionario = {'one':'um', 'two':'dois', 'three':'três'}

# 2. Como acessar os valores do dicionário
print( dicionario['one'] )
print( dicionario['two'] )
print( dicionario['three'] )
print( dicionario['four'] ) # key error - erro de chave

# 3. Como alterar os valores de um dicionário
dicionario['two'] = 'zwei'

# 4. Como adicionar valores em um dicionárip
dicionario['four'] = 'quatro'

# 5. Como verificar se a chave existe
if 'one' in dicionario:
    print("A chave existe")

# 6. Como remover um item do dicionário
meu_dicionario = {'chave1':'valor1', 'chave2':'valor2'}
meu_dicionario.pop('chave2') # del meu_dicionario['chave1']

# 7. Como limpar um dicionário
meu_dicionario = {'chave1':'valor1', 'chave2':'valor2'}
meu_dicionario.clear()

# 8. Como copiar um dicionário
meu_dicionario = {'chave1':'valor1', 'chave2':'valor2'}
outro_dicionario = meu_dicionario.copy()