# Leia 10 números do usuário, adicione-se numa lista incialmente
# vazia, remova os números pares e, ao final, ordene-os do menor
# para o maior e mostre.


def eh_par(numero):
    if numero % 2 == 0:
        return True
    return False


L = []

# Leitura
for i in range(10):
    L.append(int(input("Número: ")))

print(L)

# Remoção dos pares
nova_lista = []
for item in L:
    if not (eh_par(item)):
        nova_lista.append(item)

nova_lista.sort(reverse=False)
print(nova_lista)
