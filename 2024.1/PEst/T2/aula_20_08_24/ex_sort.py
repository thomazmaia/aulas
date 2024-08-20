# Leia 10 números do usuário, adicione-os a uma lista inicialmente vazia. Remova os números pares e, ao final, ordene-os do maior para o menor.

lista = []

# Receber dados e colocar na lista
for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

print(lista)

# Retirar números pares da lista
copia = lista[:]
for elemento in copia:
    if elemento % 2 == 0: # se par
        lista.remove(elemento)

print(lista)

# Ordenar de maneira decrescente
lista.sort(reverse=True)

print(lista)