# Ler 5 itens do usuário e:
# 7. leia mais um elemento e armazene-o na variável "A". Verifique se esse elemento está na lista e escreva a lista sem esse elemento.

L = list()
for i in range(5):
    L.append(input("Digite um elemento: "))

x = input("Digite o novo valor: ")
nova_lista = []

for elemento in L:
    if elemento == x:
        print("Ele está na lista")
    else:
        nova_lista.append(elemento)

print(nova_lista)
