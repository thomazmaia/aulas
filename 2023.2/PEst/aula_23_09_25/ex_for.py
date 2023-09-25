L1 = [8, 10, 45, 78, "a", "palavra", 0, 1, 2]
L2 = L1[:]

for indice in range(len(L1)):
    L1[indice] = 5

for elemento in L2:
    elemento = 5

print(L1)
print(L2)
