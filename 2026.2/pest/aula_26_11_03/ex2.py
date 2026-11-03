# Crie uma função que receba DOIS números e mostre a SOMA desses números.

def soma(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    res = n1 + n2
    print(f"{n1} + {n2} = {res}")

soma(3, 2)
soma(2, 3)
soma(10, 4)
soma(3, -3)
soma(4, -10)

A = input("Digite um número: ")
B = input("Digite um número: ")
soma(A, B)