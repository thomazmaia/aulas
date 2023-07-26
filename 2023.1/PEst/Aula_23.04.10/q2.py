# 2. Escreva uma função que retorne o maior de dois números.

def maximo(A, B):
    maior = 0
    if A >= B:
        maior = A
    elif B > A:
        maior = B
    return maior

print( maximo(5, 6) )
print( maximo(2, 1) )
print( maximo(7, 7) )