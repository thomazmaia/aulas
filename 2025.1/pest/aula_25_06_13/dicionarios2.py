# OUTRAS OPERAÇÕES COM DICIONÁRIOS
# 1) Verificar se a chave existe
D = {'one' : 'um', 'two' : 'dois', 'three' : 'três'}

if 'one' in D:
    print(f"A chave 'one' existe no dicionário")
else:
    print(f"A chave 'one' NÃO existe no dicionário")

if 'four' in D:
    print(f"A chave 'four' existe no dicionário")
else:
    print(f"A chave 'four' NÃO existe no dicionário")

# 2) Saber o tamanho do dicionário
D = {'one' : 'um', 'two' : 'dois', 'three' : 'três'}
print(f'O dicionário tem {len(D)} elementos')

# 3) Como remover um elemento
D = {'one' : 'um', 'two' : 'dois', 'three' : 'três'}
del D['two']
D.pop('one')
print(D)

# 4) Como zerar/limpar um dicionário
D = {'one' : 'um', 'two' : 'dois', 'three' : 'três'}
D.clear()
print(D)

# 5) Como copiar um dicionário
D = {'one' : 'um', 'two' : 'dois', 'three' : 'três'}
D2 = D.copy()
print(D)
print(D2)