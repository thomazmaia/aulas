# Adicionando elementos na lista - INSERT

L = [3, 4, 10, 4, 3, 8, 5, 0]

tamanho = len(L)
print(f"tamanho ANTES: {tamanho}")

L.insert(2, 'a')

print(L)
tamanho = len(L)
print(f"tamanho DEPOIS: {tamanho}")

L.append('z')
print(L)