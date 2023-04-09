# Ler 5 itens do usuário e:
# 2. substitua todos os elementos da lista pelo elemento "x".

L = [0, 0, 0, 0, 0]
print(L)

for i in range(5):
    L[i] = input(f"Digite o elemento {i}:")
print(L)

for i in range(5):
    L[i] = 'x'
print(L)