# Ler 5 itens do usuário e:
# 5. apague todos os elementos repetidos da lista.
# OBS: apagar NÃO é setar para ZERO e sim eliminar o termo.

L = list()
for i in range(5):
    L.append(input("Digite um elemento: "))

for elemento in L:
    vezes = L.count(elemento)
    if vezes > 1:
        for i in range(vezes):
            L.remove(elemento)
print(L)