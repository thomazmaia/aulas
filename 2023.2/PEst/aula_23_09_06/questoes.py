# 1. Escreva uma função que receba dois números e retorne o maior deles.
def questao_1():
    def verifica_maior(num1, num2):
        if num1 > num2:
            return num1
        return num2


    A = int(input("Digite o 1o número: "))
    B = int(input("Digite o 2o número: "))

    maior = verifica_maior(A, B)
    print(f"O mairo número entre {A} e {B} é {maior}")

# 2. Escreva uma função que receba três números e retorne o menor deles.

def get_menor(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        res = num1
    if num2 <= num1 and num2 <= num3:
        res = num2
    if num3 <= num2 and num3 <= num1:
        res = num3
    return res


A = int(input("Digite o 1o numero: "))
B = int(input("Digite o 2o numero: "))
C = int(input("Digite o 3o numero: "))

menor = get_menor(A, B, C)
print(f"O menor entre {A}, {B} e {C} é {menor}")
