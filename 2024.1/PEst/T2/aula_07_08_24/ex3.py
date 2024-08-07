L = [1, 2, 3, 'a', 'a', 'c']

LC = L[:]

for i in range(len(L)):
    print(L[i])
    if L[i] == 'a':
        LC.remove('a') # del L[i]
    
print(L)
print(LC)