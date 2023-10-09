# Adicionando elementos com APPEND()

L1 = [1, 2, 3]
nova_lista = L1[:]

L1.append(10)  # Adiciona ao final da lista

print(L1)
print(nova_lista)


# Adicionando elementos com INSERT()

L2 = list()
print(L2)

L2.insert(0, "oi")  # Adiciona antes do índice 0
L2.insert(1, True)  # Adiciona antes do índice 1
L2.insert(2, 0.25)  # Adiciona antes do índice 2

print(L2)

L2.insert(-1, "tchau")  # Adiciona antes do último elemento

print(L2)
