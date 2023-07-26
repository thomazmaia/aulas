# Ler 5 itens do usuário e:
# 6. informe se existem elementos repetidos nessa lista ou não.

L = list()
for i in range(5):
    L.append(input("Digite um elemento: "))

for elemento in L:
    vezes = L.count(elemento)
    if vezes > 1:
        print("Existem elementos repetidos!")
        break
print(L)