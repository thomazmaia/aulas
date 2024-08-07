# Como inserir elementos na lista - APPEND

L = [3, 5, 10, 4, 3, 8, 5, 0]

print(L)
L.append(1) 
print(L)
L.append("oi")
print(L)

# Ex:
notas = []
for i in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

print(notas)