# 1. Como criar um dicionário
dicionario = {}     # dicionário vazio
dicionario = dict() # dicionário vazio

en_ptbr = {"one" : "um", "two" : "dois","three" : "três"}

# 2. Como acessar os valores do dicionário
print(en_ptbr["one"])
print(en_ptbr["two"])
print(en_ptbr["three"])

# 3. Como alterar os valores de um dicionário
en_ptbr['two'] = 'zwei'

# 4. Como adicionar valores em um dicionário
en_ptbr['four'] = 'quatro'

# 5. Verificar se a chave existe
if 'two' in en_ptbr:
    print("A chave existe no dicionário")
else:
    print("A chave NÃO existe no dicionário")

# 6. Como remover um item de um dicionário
meu_dicionario = {'chave1' : 'valor1', 'chave2' : 'valor2'}
meu_dicionario.pop('chave2') # del meu_dicionario['chave1']

# 7. Como limpar um dicionário
meu_dicionario = {'chave1' : 'valor1', 'chave2' : 'valor2'}
meu_dicionario.clear()

# 8. Como copiar um dicionário
meu_dicionario = {'chave1' : 'valor1', 'chave2' : 'valor2'}
outro_dicionario = meu_dicionario.copy()