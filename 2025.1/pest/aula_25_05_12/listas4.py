# Percorrendo listas em Python
# 1) Usando WHILE
L = [1.5, 7, 'IFCE', 10, 5.6, 'uva']

contador = 0

print("Usando WHILE:")
while contador < len(L):
    print(L[contador])
    contador += 1

# 2) Usando FOR
print("Usando FOR:")
for i in range(len(L)):
    print(f"{i+1}o elemento: {L[i]}")

# 3) Usando FOR com items
print("Usando FOR com ITEMS")
for item in L:
    print(item)



