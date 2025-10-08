# Fatiamento de Listas (slicing)
# Fatiar é separar partes da lista de acordo com um critério que parece muito com o RANGE do FOR.
# LISTA[inicio:fim:passo]
# Obs: a fatia de uma lista é uma nova (sub)lista

L = [10, 3, 7, 80, 15, 17, 3, 66, 100, 92, 73]

# Fatiamento simples
print(L[0])
print(L[5])

# Fatiamento com intervalo
print(L[1:4])
print(L[:4])
print(L[7:])
print(L[:])

# Fatiamento com passo
print(L[::2])
print(L[1::3])
print(L[::])
print(L[7:2])
print(L[7:2:])
print(L[7:2:-1])
print(L[::-1])

# Fatiamento com índices negativos
L = [2, 4, 6, 8, 'x', 'uva']
print(L[-1]) # Último elemento
print(L[-3]) # 4
print(L[-1::-1]) # Lista invertida