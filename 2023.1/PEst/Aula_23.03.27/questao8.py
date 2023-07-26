# Ler 5 itens do usuário e:
# 8. crie uma nova lista igual à lista inicial mas sem os elementos repetidos.
# OBS: a lista inicial NÃO deve sofrer modificações.

L = list()
for i in range(5):
    L.append(input("Digite um elemento: "))

nova_lista = []

for elemento in L:
    vezes = L.count(elemento)
    if vezes == 1:
        nova_lista.append(elemento)

print(f"Antiga lista: {L}")
print(f"Nova lista: {nova_lista}")