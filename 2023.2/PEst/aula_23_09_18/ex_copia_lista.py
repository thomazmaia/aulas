# Criando listas
L1 = [1, 2, 3, 4, 5]
L2 = []

print(L1)
print(L2)

# Copiando listas (só a referência)
L2 = L1
print(L1)
print(L2)
# Modificando o 1o elemento da lista 1 também modifica o 1o elemento da lista 2
L1[0] = 6
print(L1)
print(L2)

print("Agora copiando de forma correta:")
# Copiando listas
L2 = L1[:]
print(L1)
print(L2)
# Modificando o 1o elemento da lista 1 NÃO modifica o 1o elemento da lista 2
L1[0] = 1
print(L1)
print(L2)
