# Exemplo de lista:
L = ["a", "bom", 100, 5.5, " "]

# Lista vazia
L1 = []
L2 = list()

# Acessando elementos
print(L[0]) # 'a'
print(L[3]) # 5.5

# Modificando elementos
L[0] = "x"

# Copiando listas
L1 = [1, 2, 3]
L2 = [4, 5, 6]
LC = L1
print(f"L1: {L1}")
print(f"LC: {LC}")
L1[0] = 'x'
LC[0] = 'y'
print(f"L1: {L1}")
print(f"LC: {LC}")
COPIA = L1[:]
L1[0] = 'w'
COPIA[0] = 'z'

# Fatiamento (slicing)
L = ['a', 1, 'b', 2, 'c', 3, 'd', 4]
L[::2]  # ['a', 'b', 'c', 'd']
L[1::2] # [1, 2, 3, 4]

# Percorrendo listas
L = ['a', 1, 'b', 2, 'c', 3, 'd', 4]

tamanho_da_lista = len(L)
for i in range(tamanho_da_lista):
    print(L[i])

for elemento in L:
    print(elemento)