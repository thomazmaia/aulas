# # Adicionando elementos na lista - APPEND

# L = [3, 4, 10, 4, 3, 8, 5, 0]

# tamanho_da_lista = len(L)

# print(f"Tamanho da lista ANTES do append: {tamanho_da_lista}")
# L.append('garrafa')

# tamanho_da_lista = len(L)

# print(f"Tamanho da lista DEPOIS do append: {tamanho_da_lista}")
# print(L)

# Crie uma função que receba uma lista e um elemento sozinho. Adicone esse elemento ao final dessa lista e retorne essa lista com esse novo elemento.

def add_to_lista(L : list, elemento):
    L.append(elemento)
    return L


minha_lista = ['a', 'b', 'c']

print(f"Lista antes: {minha_lista}")

print(f"Lista depois: {add_to_lista(minha_lista, 4)}")