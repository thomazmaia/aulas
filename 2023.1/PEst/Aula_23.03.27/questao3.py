# Ler 5 itens do usuário e:
# 3. leia mais dois elementos, armazene-os nas variáveis "A" e "B" e, em seguida, subtituia todos os elementos da lista iguais ao valor de "A" pelo valor de "B".

L = []
a = input("Digite o elemento 1: ")
b = input("Digite o elemento 2: ")
c = input("Digite o elemento 3: ")
d = input("Digite o elemento 4: ")
e = input("Digite o elemento 5: ")
print(L)
L.append(a)
L.append(b)
L.append(c)
L.append(d)
L.append(e)
print(L)

x = input("Digite o novo elemento: ")
y = input("Digite o novo elemento: ")

if L[0] == x:
    L[0] = y
if L[1] == x:
    L[1] = y
if L[2] == x:
    L[2] = y
if L[3] == x:
    L[3] = y
if L[4] == x:
    L[4] = y
print(L)