L = [1, 2, 3, 4, 5]

# Fatiamento simples
print(L[0])  # primeiro elemento
print(L[1])  # segundo elemento
print(L[-1])  # último elemento
print(L[-2])  # penúltimo elemento

# Fatiamento com intervalo
print(L[1:4])  # elementos do índice 1 a 3
print(L[:4])  # elementos do início até o índice 3
print(L[2:])  # elementos do índice 2 até o fim
print(L[:])  # todos os elementos

# Fatiamento com passo
print(L[::2])  # todos os elementos (do início ao fim) variando de dois em dois
print(L[1::2])  # elementos do índice 1 até o fim, variando de dois em dois
print(L[0:-1:2])  # todos os elementos (do ínicio ao fim), variando de dois em dois

# Fatiamento inverso
print(L[-3:])  # os três últimos elementos
print(L[:-2])  # todos os elementos, exceto os dois últimos
