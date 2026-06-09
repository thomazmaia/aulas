# Crie um programa que peça N números inteiros ao usuário e armazene-os em uma lista. Crie também uma função que deve receber essa lista de números inteiros e retornar a quantidade de números pares nessa lista.

def eh_par(N):
    if N % 2 == 0:
        return True
    return False


def conta_pares(L : list):
    contador = 0
    for i in range(len(L)):
        if eh_par(L[i]):
            contador += 1
    return contador



print(eh_par(10))
N = int(input("Quantos elementos você quer? "))

lista = []

for i in range(N):
    numero = int(input(f"Digite o {i+1}o numero: "))
    lista.append(numero)

print(lista)
print(conta_pares(lista))