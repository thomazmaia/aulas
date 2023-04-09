# Ler 5 itens do usuário e:
# 4. leia mais 5 elementos do usuário e crie uma segunda lista. Troque os valores entre as listas "lista1" e "lista2" (elemento a elemento!).

lista1 = list()
for i in range(5):
    lista1.append(input(f"Digite o elemento {i} da lista1: "))

lista2 = list()
for i in range(5):
    lista2.append(input(f"Digite o elemento {i} da lista2: "))

print("ANTES:")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
for i in range(5):
    aux = lista2[i]
    lista2[i] = lista1[i]
    lista1[i] = aux

print("DEPOIS:")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")