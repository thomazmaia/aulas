# 1. Criando listas
L1 = [] # lista vazia
L2 = [1, 2, 3] # lista com números
L3 = ["a", "abacaxi", "@#$%ˆ&*()"] # lista com strings
L4 = [1, 2, 3.5, 67.1, "oi", " ", "@#$"] # lista mista

print(L1)
print(L2)
print(L3)
print(L4)

# 2. Acessando elementos de lista
L = [1, 2, "oi", "aux", "kkk", 0, -100]
print(L[0])  # 1
print(L[-1]) # -100

tamanho_da_lista = len(L) # 7

for item in L:
    print(item)

for i in range(tamanho_da_lista):
    print(L[i])


# 3. Modificando elementos da lista
L = [1, 2, "oi", "aux", "kkk", 0, -100]

L[0] = L[1] # 2

# 4. Fatiamento de listas
L = [1, 2, "oi", "aux", "kkk", 0, -100]

L[::2] # [1, 'oi', 'kkk', -100]

# 5. Copiando listas
L1 = [1, 2, 3, 4, 5]
L2 = L1

L2[0] = "a"

print(L1)
print(L2)

L1 = [1, 2, 3, 4, 5]
L2 = L1[:]

L2[0] = "a"
print(L1)
print(L2)